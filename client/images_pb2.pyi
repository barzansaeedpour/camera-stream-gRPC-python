from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Image(_message.Message):
    __slots__ = ("width", "height", "img")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IMG_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    img: bytes
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., img: _Optional[bytes] = ...) -> None: ...

class GetImagesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetImagesResponse(_message.Message):
    __slots__ = ("images",)
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    images: _containers.RepeatedCompositeFieldContainer[Image]
    def __init__(self, images: _Optional[_Iterable[_Union[Image, _Mapping]]] = ...) -> None: ...

class GetImageByIdRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetImageByIdResponse(_message.Message):
    __slots__ = ("Image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    Image: Image
    def __init__(self, Image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class CreateImageRequest(_message.Message):
    __slots__ = ("Image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    Image: Image
    def __init__(self, Image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class CreateImageResponse(_message.Message):
    __slots__ = ("Image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    Image: Image
    def __init__(self, Image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class UpdateImageRequest(_message.Message):
    __slots__ = ("Image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    Image: Image
    def __init__(self, Image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class UpdateImageResponse(_message.Message):
    __slots__ = ("Image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    Image: Image
    def __init__(self, Image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class DeleteImageRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteImageResponse(_message.Message):
    __slots__ = ("Image",)
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    Image: Image
    def __init__(self, Image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...
