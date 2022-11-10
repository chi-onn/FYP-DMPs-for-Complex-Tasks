
"use strict";

let ClearErr = require('./ClearErr.js')
let GripperState = require('./GripperState.js')
let TCPOffset = require('./TCPOffset.js')
let GripperConfig = require('./GripperConfig.js')
let SetString = require('./SetString.js')
let PlayTraj = require('./PlayTraj.js')
let GetFloat32List = require('./GetFloat32List.js')
let SetMultipleInts = require('./SetMultipleInts.js')
let SetLoad = require('./SetLoad.js')
let SetFloat32 = require('./SetFloat32.js')
let MoveVelo = require('./MoveVelo.js')
let ConfigToolModbus = require('./ConfigToolModbus.js')
let SetDigitalIO = require('./SetDigitalIO.js')
let Move = require('./Move.js')
let GetErr = require('./GetErr.js')
let GetDigitalIO = require('./GetDigitalIO.js')
let SetControllerAnalogIO = require('./SetControllerAnalogIO.js')
let GetSetModbusData = require('./GetSetModbusData.js')
let MoveAxisAngle = require('./MoveAxisAngle.js')
let SetInt16 = require('./SetInt16.js')
let GetControllerDigitalIO = require('./GetControllerDigitalIO.js')
let GripperMove = require('./GripperMove.js')
let GetAnalogIO = require('./GetAnalogIO.js')
let SetAxis = require('./SetAxis.js')
let SetToolModbus = require('./SetToolModbus.js')
let MoveVelocity = require('./MoveVelocity.js')
let SetModbusTimeout = require('./SetModbusTimeout.js')
let GetInt32 = require('./GetInt32.js')

module.exports = {
  ClearErr: ClearErr,
  GripperState: GripperState,
  TCPOffset: TCPOffset,
  GripperConfig: GripperConfig,
  SetString: SetString,
  PlayTraj: PlayTraj,
  GetFloat32List: GetFloat32List,
  SetMultipleInts: SetMultipleInts,
  SetLoad: SetLoad,
  SetFloat32: SetFloat32,
  MoveVelo: MoveVelo,
  ConfigToolModbus: ConfigToolModbus,
  SetDigitalIO: SetDigitalIO,
  Move: Move,
  GetErr: GetErr,
  GetDigitalIO: GetDigitalIO,
  SetControllerAnalogIO: SetControllerAnalogIO,
  GetSetModbusData: GetSetModbusData,
  MoveAxisAngle: MoveAxisAngle,
  SetInt16: SetInt16,
  GetControllerDigitalIO: GetControllerDigitalIO,
  GripperMove: GripperMove,
  GetAnalogIO: GetAnalogIO,
  SetAxis: SetAxis,
  SetToolModbus: SetToolModbus,
  MoveVelocity: MoveVelocity,
  SetModbusTimeout: SetModbusTimeout,
  GetInt32: GetInt32,
};
