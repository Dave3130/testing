# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1ll11l1l_opy_, bstack1lll1l111l1_opy_
class bstack1lll1ll111l_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11ll_opy_ (u"࡙ࠦ࡫ࡳࡵࡊࡲࡳࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᓽ").format(self.name)
class bstack1lll1l1ll11_opy_(Enum):
    NONE = 0
    BEFORE_ALL = 1
    LOG = 2
    SETUP_FIXTURE = 3
    INIT_TEST = 4
    BEFORE_EACH = 5
    AFTER_EACH = 6
    TEST = 7
    STEP = 8
    LOG_REPORT = 9
    AFTER_ALL = 10
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack11ll_opy_ (u"࡚ࠧࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᓾ").format(self.name)
class bstack1llll1111l1_opy_(bstack1ll1ll11l1l_opy_):
    bstack1ll111ll111_opy_: List[str]
    bstack1l1lllll1ll_opy_: Dict[str, str]
    state: bstack1lll1l1ll11_opy_
    bstack1ll1lllllll_opy_: datetime
    bstack1l11111l11l_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1l111l1_opy_,
        bstack1ll111ll111_opy_: List[str],
        bstack1l1lllll1ll_opy_: Dict[str, str],
        state=bstack1lll1l1ll11_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll111ll111_opy_ = bstack1ll111ll111_opy_
        self.bstack1l1lllll1ll_opy_ = bstack1l1lllll1ll_opy_
        self.state = state
        self.bstack1ll1lllllll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l11111l11l_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llllll1lll_opy_(self, bstack1l11111l111_opy_: bstack1lll1l1ll11_opy_):
        bstack1l11111l1l1_opy_ = bstack1lll1l1ll11_opy_(bstack1l11111l111_opy_).name
        if not bstack1l11111l1l1_opy_:
            return False
        if bstack1l11111l111_opy_ == self.state:
            return False
        self.state = bstack1l11111l111_opy_
        self.bstack1l11111l11l_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll11ll1111_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll11l111l1_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll111111ll_opy_: int = None
    bstack1ll11ll1l11_opy_: str = None
    bstack1lllll_opy_: str = None
    bstack1l11lllll_opy_: str = None
    bstack1ll111lll1l_opy_: str = None
    bstack1l1llll1lll_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llll111l11_opy_ = bstack11ll_opy_ (u"ࠨࡴࡦࡵࡷࡣࡺࡻࡩࡥࠤᓿ")
    bstack1ll11111ll1_opy_ = bstack11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡯ࡤࠣᔀ")
    bstack1ll11ll1ll1_opy_ = bstack11ll_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡮ࡢ࡯ࡨࠦᔁ")
    bstack1ll1111llll_opy_ = bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡤࡶࡡࡵࡪࠥᔂ")
    bstack1ll11111l1l_opy_ = bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡶࡤ࡫ࡸࠨᔃ")
    bstack1lll11ll11l_opy_ = bstack11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡸࡻ࡬ࡵࠤᔄ")
    bstack1ll11l1ll11_opy_ = bstack11ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡹࡵ࡭ࡶࡢࡥࡹࠨᔅ")
    bstack1ll1l11l111_opy_ = bstack11ll_opy_ (u"ࠨࡴࡦࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᔆ")
    bstack1l1lllll11l_opy_ = bstack11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᔇ")
    bstack1ll111l11l1_opy_ = bstack11ll_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᔈ")
    bstack1lll1lllll1_opy_ = bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠣᔉ")
    bstack1lll1l11111_opy_ = bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧᔊ")
    bstack1ll1111lll1_opy_ = bstack11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡦࡳࡩ࡫ࠢᔋ")
    bstack1ll111ll11l_opy_ = bstack11ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠢᔌ")
    bstack1llll1l111l_opy_ = bstack11ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࠢᔍ")
    bstack1lll1l1111l_opy_ = bstack11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡡࡪ࡮ࡸࡶࡪࠨᔎ")
    bstack1l1llll1111_opy_ = bstack11ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠧᔏ")
    bstack1ll1l1l11l1_opy_ = bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡭ࡱࡪࡷࠧᔐ")
    bstack1l1llllll11_opy_ = bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡠ࡯ࡨࡸࡦࠨᔑ")
    bstack1l11111l1ll_opy_ = bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡶࡧࡴࡶࡥࡴࠩᔒ")
    bstack1lll11l111l_opy_ = bstack11ll_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨᔓ")
    bstack1ll11l1l111_opy_ = bstack11ll_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᔔ")
    bstack1ll11l11111_opy_ = bstack11ll_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡥ࡯ࡦࡨࡨࡤࡧࡴࠣᔕ")
    bstack1ll1l11ll1l_opy_ = bstack11ll_opy_ (u"ࠣࡪࡲࡳࡰࡥࡩࡥࠤᔖ")
    bstack1l1lllll111_opy_ = bstack11ll_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡳࡧࡶࡹࡱࡺࠢᔗ")
    bstack1l1lll1ll11_opy_ = bstack11ll_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠ࡮ࡲ࡫ࡸࠨᔘ")
    bstack1ll1l11l11l_opy_ = bstack11ll_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠢᔙ")
    bstack1ll111l1l11_opy_ = bstack11ll_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᔚ")
    bstack1ll1111l111_opy_ = bstack11ll_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠣᔛ")
    bstack1ll1l111111_opy_ = bstack11ll_opy_ (u"ࠢࡱࡧࡱࡨ࡮ࡴࡧࠣᔜ")
    bstack1ll111l1lll_opy_ = bstack11ll_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤᔝ")
    bstack1l111lll11l_opy_ = bstack11ll_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࠦᔞ")
    bstack1ll1l1l1l11_opy_ = bstack11ll_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡎࡒࡋࠧᔟ")
    bstack1l11l1l1111_opy_ = bstack11ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᔠ")
    bstack1lll1l11ll1_opy_: Dict[str, bstack1llll1111l1_opy_] = dict()
    bstack1l111111ll1_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll111ll111_opy_: List[str]
    bstack1l1lllll1ll_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll111ll111_opy_: List[str],
        bstack1l1lllll1ll_opy_: Dict[str, str],
        bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_
    ):
        self.bstack1ll111ll111_opy_ = bstack1ll111ll111_opy_
        self.bstack1l1lllll1ll_opy_ = bstack1l1lllll1ll_opy_
        self.bstack1lll11l1l1l_opy_ = bstack1lll11l1l1l_opy_
    def track_event(
        self,
        context: bstack1ll11ll1111_opy_,
        test_framework_state: bstack1lll1l1ll11_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack11ll_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࢃࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠥࡧࡲࡨࡵࡀࡿࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻࡾࠤᔡ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll1l1ll11l_opy_(
        self,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1lll1l_opy_ = TestFramework.bstack1l1ll1l1l11_opy_(bstack1lllll1l11l_opy_)
        if not bstack1l1ll1lll1l_opy_ in TestFramework.bstack1l111111ll1_opy_:
            return
        self.logger.debug(bstack11ll_opy_ (u"ࠨࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡽࢀࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡹࠢᔢ").format(len(TestFramework.bstack1l111111ll1_opy_[bstack1l1ll1lll1l_opy_])))
        for callback in TestFramework.bstack1l111111ll1_opy_[bstack1l1ll1lll1l_opy_]:
            try:
                callback(self, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack11ll_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠢᔣ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll1l1l111l_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll11ll11ll_opy_(self, instance, bstack1lllll1l11l_opy_):
        return
    @abc.abstractmethod
    def bstack1ll11llll11_opy_(self, instance, bstack1lllll1l11l_opy_):
        return
    @staticmethod
    def bstack1ll11l1lll1_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1ll11l1l_opy_.create_context(target)
        instance = TestFramework.bstack1lll1l11ll1_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll11l11_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l111llll11_opy_(reverse=True) -> List[bstack1llll1111l1_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll1l11ll1_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lllllll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l111ll1lll_opy_(ctx: bstack1lll1l111l1_opy_, reverse=True) -> List[bstack1llll1111l1_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll1l11ll1_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lllllll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllllll111_opy_(instance: bstack1llll1111l1_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llll1111l1_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llllll1lll_opy_(instance: bstack1llll1111l1_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11ll_opy_ (u"ࠣࡵࡨࡸࡤࡹࡴࡢࡶࡨ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣ࡯ࡪࡿ࠽ࡼࡿࠣࡺࡦࡲࡵࡦ࠿ࡾࢁࠧᔤ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11lllll1_opy_(instance: bstack1llll1111l1_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack11ll_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩࡤ࡫࡮ࡵࡴ࡬ࡩࡸࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾࢁࠥ࡫࡮ࡵࡴ࡬ࡩࡸࡃࡻࡾࠤᔥ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l111111lll_opy_(instance: bstack1lll1l1ll11_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11ll_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡽࠡ࡭ࡨࡽࡂࢁࡽࠡࡸࡤࡰࡺ࡫࠽ࡼࡿࠥᔦ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll11l1lll1_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll11l1lll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1l1llll11l1_opy_(instance: bstack1llll1111l1_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll11l1111l_opy_(instance: bstack1llll1111l1_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1ll1l1l11_opy_(bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_]):
        return bstack11ll_opy_ (u"ࠦ࠿ࠨᔧ").join((bstack1lll1l1ll11_opy_(bstack1lllll1l11l_opy_[0]).name, bstack1lll1ll111l_opy_(bstack1lllll1l11l_opy_[1]).name))
    @staticmethod
    def bstack1lllll1l1ll_opy_(bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_], callback: Callable):
        bstack1l1ll1lll1l_opy_ = TestFramework.bstack1l1ll1l1l11_opy_(bstack1lllll1l11l_opy_)
        TestFramework.logger.debug(bstack11ll_opy_ (u"ࠧࡹࡥࡵࡡ࡫ࡳࡴࡱ࡟ࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣ࡬ࡴࡵ࡫ࡠࡴࡨ࡫࡮ࡹࡴࡳࡻࡢ࡯ࡪࡿ࠽ࡼࡿࠥᔨ").format(bstack1l1ll1lll1l_opy_))
        if not bstack1l1ll1lll1l_opy_ in TestFramework.bstack1l111111ll1_opy_:
            TestFramework.bstack1l111111ll1_opy_[bstack1l1ll1lll1l_opy_] = []
        TestFramework.bstack1l111111ll1_opy_[bstack1l1ll1lll1l_opy_].append(callback)
    @staticmethod
    def bstack1ll111l111l_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡸ࡮ࡴࡳࠣᔩ"):
            return klass.__qualname__
        return module + bstack11ll_opy_ (u"ࠢ࠯ࠤᔪ") + klass.__qualname__
    @staticmethod
    def bstack1ll1l11lll1_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}