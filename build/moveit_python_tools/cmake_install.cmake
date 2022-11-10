# Install script for directory: /home/chionn/fyp_ws/src/moveit_python_tools

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/chionn/fyp_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/chionn/fyp_ws/build/moveit_python_tools/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/chionn/fyp_ws/build/moveit_python_tools/catkin_generated/installspace/moveit_python_tools.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_python_tools/cmake" TYPE FILE FILES
    "/home/chionn/fyp_ws/build/moveit_python_tools/catkin_generated/installspace/moveit_python_toolsConfig.cmake"
    "/home/chionn/fyp_ws/build/moveit_python_tools/catkin_generated/installspace/moveit_python_toolsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_python_tools" TYPE FILE FILES "/home/chionn/fyp_ws/src/moveit_python_tools/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/moveit_python_tools" TYPE PROGRAM FILES
    "/home/chionn/fyp_ws/src/moveit_python_tools/scripts/go_to_joint_cfg.py"
    "/home/chionn/fyp_ws/src/moveit_python_tools/scripts/pr2_get_ik.py"
    "/home/chionn/fyp_ws/src/moveit_python_tools/scripts/pr2_get_ik_and_go.py"
    "/home/chionn/fyp_ws/src/moveit_python_tools/scripts/tf_for_me.py"
    "/home/chionn/fyp_ws/src/moveit_python_tools/scripts/joystick_teleop.py"
    "/home/chionn/fyp_ws/src/moveit_python_tools/scripts/pr2_go_to_topic_pose_fjt.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/moveit_python_tools/launch" TYPE DIRECTORY FILES "/home/chionn/fyp_ws/src/moveit_python_tools/launch/")
endif()

