__author__ = 'marko'

import sys
import os
import cv2
from argparse import ArgumentParser
from modules.faceswap import swap_faces


def main(img1_path, img2_path, output_path, show=False):
    img1, img2 = map(cv2.imread, [img1_path, img2_path])
    output_img = swap_faces(img1, img2)

    if show:
        cv2.imshow('output_img', output_img)
        if cv2.waitKey(0) > 30:
            pass

    cv2.imwrite(output_path, output_img)
    print 'Output image stored to %s' % output_path
    print 'Completed'

if __name__ == '__main__':
    parser = ArgumentParser(description='faceswap')
    parser.add_argument('img1_path', help='path to first image (head)')
    parser.add_argument('img2_path', help='path to second image (face)')
    parser.add_argument('-o', '--output', help='path for output image', default='output.jpg')
    parser.add_argument('--show', help='display output image', action="store_true")

    args = parser.parse_args()

    if not os.path.isfile(args.img1_path) or not os.path.isfile(args.img2_path):
        print 'Arguments not valid'
        parser.print_help()
        parser.exit()

    main(args.img1_path, args.img2_path, args.output, args.show)
