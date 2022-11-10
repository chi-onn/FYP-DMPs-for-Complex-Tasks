#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/chionn/fyp_ws/src/moveit_python_tools"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/chionn/fyp_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/chionn/fyp_ws/install/lib/python3/dist-packages:/home/chionn/fyp_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/chionn/fyp_ws/build" \
    "/usr/bin/python3" \
    "/home/chionn/fyp_ws/src/moveit_python_tools/setup.py" \
     \
    build --build-base "/home/chionn/fyp_ws/build/moveit_python_tools" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/chionn/fyp_ws/install" --install-scripts="/home/chionn/fyp_ws/install/bin"
