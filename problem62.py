#!/usr/bin/env python

if __name__ == '__main__':
    cubes = {}
    n = 1
    while True:
        next_cube = str(n * n * n)
        key = ''.join(sorted(next_cube))
        cube_list = cubes.get(key, [])
        cube_list.append(next_cube)
        cubes[key] = cube_list
        if len(cube_list) == 5:
            print str(sorted(cube_list))
            import sys; sys.exit(0)
        n += 1
