import h5py
import argparse


def merge(output, h5s):
    try:
        dfs = [h5py.File(h5, "r") for h5 in h5s]

        im_key = list(dfs[0].keys())[0] + "/images"
        im_shape = dfs[0][im_key].shape[1:]
        merged_shape = [0] + list(im_shape)
        for df in dfs:
            assert df[im_key].shape[1:] == im_shape, "Image shape in %s (%s) does not equal %s" % (df.filename, str(df[im_key].shape[1:]), str(im_shape))
            merged_shape[0] += df[im_key].shape[0]

        merged_shape = tuple(merged_shape)

        with h5py.File(output, "w") as merged_df: 
            for changrp in dfs[0].keys():
                mergedgrp = merged_df.create_group(changrp)
                for key in dfs[0][changrp].keys():
                    layout = h5py.VirtualLayout(shape=merged_shape, dtype=dfs[0][changrp][key].dtype)
                    vsources = []
                    i = 0
                    for df in dfs:
                        vsources.append(h5py.VirtualSource(df[changrp+"/"+key]))
                        layout[i:i+vsources[-1].shape[0]] = vsources[-1]

                        i += vsources[-1].shape[0]

                    mergedgrp.create_virtual_dataset(key, layout)

    finally:
        for df in dfs:
            df.close()


def main():
    parser = argparse.ArgumentParser(prog="cifconvert")
    parser.add_argument(
        "output", type=str,
        help="Output filename for h5."
    )
    parser.add_argument(
        "h5s", type=str,
        help="h5 datasets to concatenate in virtual dataset.", nargs="*")

    flags = parser.parse_args()

    merge(**vars(flags))


if __name__ == "__main__":
    main()


