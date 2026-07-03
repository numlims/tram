# automatically generated, DON'T EDIT. please edit main.ct from where this file stems.
import argparse
import versionflag
import sys
def main():
    """
     main adds a version flag.
    """
    parser = argparse.ArgumentParser(description="hdrp models")
    versionflag.flag(parser, "tram")
    args = parser.parse_args()
sys.exit(main())
