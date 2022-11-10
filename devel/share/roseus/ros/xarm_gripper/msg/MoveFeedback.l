;; Auto-generated. Do not edit!


(when (boundp 'xarm_gripper::MoveFeedback)
  (if (not (find-package "XARM_GRIPPER"))
    (make-package "XARM_GRIPPER"))
  (shadow 'MoveFeedback (find-package "XARM_GRIPPER")))
(unless (find-package "XARM_GRIPPER::MOVEFEEDBACK")
  (make-package "XARM_GRIPPER::MOVEFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude MoveFeedback.msg.html


(defclass xarm_gripper::MoveFeedback
  :super ros::object
  :slots (_current_pulse ))

(defmethod xarm_gripper::MoveFeedback
  (:init
   (&key
    ((:current_pulse __current_pulse) 0.0)
    )
   (send-super :init)
   (setq _current_pulse (float __current_pulse))
   self)
  (:current_pulse
   (&optional __current_pulse)
   (if __current_pulse (setq _current_pulse __current_pulse)) _current_pulse)
  (:serialization-length
   ()
   (+
    ;; float32 _current_pulse
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _current_pulse
       (sys::poke _current_pulse (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _current_pulse
     (setq _current_pulse (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get xarm_gripper::MoveFeedback :md5sum-) "a244e071efec9946f249ffbbf7ee56b0")
(setf (get xarm_gripper::MoveFeedback :datatype-) "xarm_gripper/MoveFeedback")
(setf (get xarm_gripper::MoveFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

float32 current_pulse


")



(provide :xarm_gripper/MoveFeedback "a244e071efec9946f249ffbbf7ee56b0")

