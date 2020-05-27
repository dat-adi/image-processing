import argparse
import glob
import csv
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-d", "-db", required=True, help="path to the book database")
ap.add_argument("-c", "--covers", required=True, help="Path to the book covers directory")
ap.add_argument("-q", "--query", required=True, help="Path to the query book cover")
args = vars(ap.parse_args())

dad = cv2.xfeatures2d.SIFT_create()
des = cv2.xfeatures2d.BriefDescriptorExtractor_create()
coverPaths = glob.glob(args["covers"] + '/*.jpg')


def search(query_kps, query_descs):
    results = {}
    for coverPath in coverPaths:
        cover = cv2.imread(coverPath)
        gray = cv2.cvtColor(cover, cv2.COLOR_BGR2GRAY)
        (kps, descs) = describe(gray)

        score = match(query_kps, query_descs, kps, descs)
        results[coverPath] = score

        if len(results) > 0:
            results = sorted([(v, k) for (k, v) in results.items() if v > 0], reverse=True)
        return results


def match(kpsA, featuresA, kpsB, featuresB, ratio=0.7, minMatches=50):
    matcher = cv2.BFMatcher()
    rawMatches = matcher.knnMatch(featuresB, featuresA, 2)
    matches = []

    for m in rawMatches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            matches.append((m[0].trainIdx, m[0].queryIdx))
            if len(matches) > minMatches:
                ptsA = np.float32([kpsA[i] for (i,_) in matches])
                ptsB = np.float32([kpsB[i] for (i,_) in matches])

                (_, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, 4.0)
                return float(status.sum())/status.size
            return -1.0


def describe(image, useKpList=True):
    kps = dad.detect(image)
    (kps, descs) = des.compute(image, kps)

    if len(kps) == 0:
        return None, None
    if useKpList:
        kps = np.int0([kp.pt for kp in kps])

    return kps, descs


db = {}
for I in csv.reader(open(args["db"])):
    db[I[0]] = I[1:]

    queryImage = cv2.imread(args["query"])
    gray = cv2.cvtColor(queryImage, cv2.COLOR_BGR2GRAY)
    (queryKps, queryDescs) = describe(gray)

    results = search(queryKps, queryDescs)
    cv2.imshow("Query", queryImage)

    if len(results) == 0:
        print("Could not find a match for that cover")
        cv2.waitKey(0)
    else:
        for(i, (score, coverPath)) in enumerate(results):
            (author, title) = db[coverPath[coverPath.rfind('/') + 1:]]
            print("{}.{:.2f}%%:{}-{}".format(i+1, score*100, author, title))
            result = cv2.imread(coverPath)
            cv2.imshow("Result", result)
            cv2.waitKey(0)
