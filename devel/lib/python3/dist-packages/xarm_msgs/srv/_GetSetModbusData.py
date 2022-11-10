# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from xarm_msgs/GetSetModbusDataRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetSetModbusDataRequest(genpy.Message):
  _md5sum = "0df4146f0963d1cf15d364518c202d50"
  _type = "xarm_msgs/GetSetModbusDataRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# unsigned char data to be sent to tool device through modbus
uint8[] send_data

# Specify the anticipated maximum respond data length in bytes
int16 respond_len

# host id, 9: END RS485, 10: Controller RS485
uint8 host_id

# whether to choose transparent transmission
bool is_transparent_transmission

# whether to use port 503 for communication
# if it is true, it will connect to 503 port for communication when it is used for the first time, which is generally only useful for transparent transmission
bool use_503_port

"""
  __slots__ = ['send_data','respond_len','host_id','is_transparent_transmission','use_503_port']
  _slot_types = ['uint8[]','int16','uint8','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       send_data,respond_len,host_id,is_transparent_transmission,use_503_port

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetSetModbusDataRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.send_data is None:
        self.send_data = b''
      if self.respond_len is None:
        self.respond_len = 0
      if self.host_id is None:
        self.host_id = 0
      if self.is_transparent_transmission is None:
        self.is_transparent_transmission = False
      if self.use_503_port is None:
        self.use_503_port = False
    else:
      self.send_data = b''
      self.respond_len = 0
      self.host_id = 0
      self.is_transparent_transmission = False
      self.use_503_port = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.send_data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_h3B().pack(_x.respond_len, _x.host_id, _x.is_transparent_transmission, _x.use_503_port))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.send_data = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.respond_len, _x.host_id, _x.is_transparent_transmission, _x.use_503_port,) = _get_struct_h3B().unpack(str[start:end])
      self.is_transparent_transmission = bool(self.is_transparent_transmission)
      self.use_503_port = bool(self.use_503_port)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.send_data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_h3B().pack(_x.respond_len, _x.host_id, _x.is_transparent_transmission, _x.use_503_port))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.send_data = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.respond_len, _x.host_id, _x.is_transparent_transmission, _x.use_503_port,) = _get_struct_h3B().unpack(str[start:end])
      self.is_transparent_transmission = bool(self.is_transparent_transmission)
      self.use_503_port = bool(self.use_503_port)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_h3B = None
def _get_struct_h3B():
    global _struct_h3B
    if _struct_h3B is None:
        _struct_h3B = struct.Struct("<h3B")
    return _struct_h3B
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from xarm_msgs/GetSetModbusDataResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetSetModbusDataResponse(genpy.Message):
  _md5sum = "6758d9ca75742796b3adadfd14ca06e2"
  _type = "xarm_msgs/GetSetModbusDataResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
int16 ret
string message
uint8[] respond_data
"""
  __slots__ = ['ret','message','respond_data']
  _slot_types = ['int16','string','uint8[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ret,message,respond_data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetSetModbusDataResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ret is None:
        self.ret = 0
      if self.message is None:
        self.message = ''
      if self.respond_data is None:
        self.respond_data = b''
    else:
      self.ret = 0
      self.message = ''
      self.respond_data = b''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.ret
      buff.write(_get_struct_h().pack(_x))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.respond_data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 2
      (self.ret,) = _get_struct_h().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.respond_data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.ret
      buff.write(_get_struct_h().pack(_x))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.respond_data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 2
      (self.ret,) = _get_struct_h().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.respond_data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_h = None
def _get_struct_h():
    global _struct_h
    if _struct_h is None:
        _struct_h = struct.Struct("<h")
    return _struct_h
class GetSetModbusData(object):
  _type          = 'xarm_msgs/GetSetModbusData'
  _md5sum = 'dc342acff6bdfadcdcdb95fac36d565f'
  _request_class  = GetSetModbusDataRequest
  _response_class = GetSetModbusDataResponse
