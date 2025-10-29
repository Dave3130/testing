# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l111l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1ll11111_opy_, bstack1lll1l1l1ll_opy_
class bstack1lll11lll1l_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11ll1l_opy_ (u"ࠣࡖࡨࡷࡹࡎ࡯ࡰ࡭ࡖࡸࡦࡺࡥ࠯ࡽࢀࠦᔈ").format(self.name)
class bstack1lll1l1l11l_opy_(Enum):
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
        return bstack11ll1l_opy_ (u"ࠤࡗࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥᔉ").format(self.name)
class bstack1lll1l11lll_opy_(bstack1ll1ll11111_opy_):
    bstack1ll111l11l1_opy_: List[str]
    bstack1ll11ll1111_opy_: Dict[str, str]
    state: bstack1lll1l1l11l_opy_
    bstack1ll1lllll11_opy_: datetime
    bstack1l1111111ll_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1l1l1ll_opy_,
        bstack1ll111l11l1_opy_: List[str],
        bstack1ll11ll1111_opy_: Dict[str, str],
        state=bstack1lll1l1l11l_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll111l11l1_opy_ = bstack1ll111l11l1_opy_
        self.bstack1ll11ll1111_opy_ = bstack1ll11ll1111_opy_
        self.state = state
        self.bstack1ll1lllll11_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111111ll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll1l1lll_opy_(self, bstack1l111111ll1_opy_: bstack1lll1l1l11l_opy_):
        bstack1l111111l11_opy_ = bstack1lll1l1l11l_opy_(bstack1l111111ll1_opy_).name
        if not bstack1l111111l11_opy_:
            return False
        if bstack1l111111ll1_opy_ == self.state:
            return False
        self.state = bstack1l111111ll1_opy_
        self.bstack1l1111111ll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll1l1l11l1_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll11lll11l_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll111ll1ll_opy_: int = None
    bstack1ll111lll1l_opy_: str = None
    bstack1l1ll_opy_: str = None
    bstack1l11111ll_opy_: str = None
    bstack1ll1l111l11_opy_: str = None
    bstack1l1llllll1l_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1lllll1_opy_ = bstack11ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡷࡸ࡭ࡩࠨᔊ")
    bstack1ll11l1111l_opy_ = bstack11ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡬ࡨࠧᔋ")
    bstack1ll11111l1l_opy_ = bstack11ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡲࡦࡳࡥࠣᔌ")
    bstack1ll1l1111l1_opy_ = bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡡࡳࡥࡹ࡮ࠢᔍ")
    bstack1ll111111ll_opy_ = bstack11ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡺࡡࡨࡵࠥᔎ")
    bstack1lll1l11111_opy_ = bstack11ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡦࡵࡸࡰࡹࠨᔏ")
    bstack1ll1111l1ll_opy_ = bstack11ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡶࡹࡱࡺ࡟ࡢࡶࠥᔐ")
    bstack1ll11l1ll11_opy_ = bstack11ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᔑ")
    bstack1ll111ll1l1_opy_ = bstack11ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡨࡲࡩ࡫ࡤࡠࡣࡷࠦᔒ")
    bstack1ll1111lll1_opy_ = bstack11ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡰࡴࡩࡡࡵ࡫ࡲࡲࠧᔓ")
    bstack1llll111l11_opy_ = bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠧᔔ")
    bstack1lll1l1lll1_opy_ = bstack11ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤᔕ")
    bstack1l1lll1ll11_opy_ = bstack11ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡣࡰࡦࡨࠦᔖ")
    bstack1l1lll1llll_opy_ = bstack11ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠦᔗ")
    bstack1lllll1llll_opy_ = bstack11ll1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠦᔘ")
    bstack1lll1l11l11_opy_ = bstack11ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩࡥ࡮ࡲࡵࡳࡧࠥᔙ")
    bstack1ll1l11l1ll_opy_ = bstack11ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠤᔚ")
    bstack1ll11ll111l_opy_ = bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡱࡵࡧࡴࠤᔛ")
    bstack1ll1l11llll_opy_ = bstack11ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡳࡥࡵࡣࠥᔜ")
    bstack1l111111lll_opy_ = bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡳࡤࡱࡳࡩࡸ࠭ᔝ")
    bstack1ll1llllll1_opy_ = bstack11ll1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᔞ")
    bstack1ll11llll1l_opy_ = bstack11ll1l_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᔟ")
    bstack1ll1l11ll1l_opy_ = bstack11ll1l_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡩࡳࡪࡥࡥࡡࡤࡸࠧᔠ")
    bstack1ll11l1l111_opy_ = bstack11ll1l_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢ࡭ࡩࠨᔡ")
    bstack1ll11l1ll1l_opy_ = bstack11ll1l_opy_ (u"ࠨࡨࡰࡱ࡮ࡣࡷ࡫ࡳࡶ࡮ࡷࠦᔢ")
    bstack1ll111l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡲ࡯ࡨࡵࠥᔣ")
    bstack1l1llll1111_opy_ = bstack11ll1l_opy_ (u"ࠣࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠦᔤ")
    bstack1ll11ll1ll1_opy_ = bstack11ll1l_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᔥ")
    bstack1l1llll11l1_opy_ = bstack11ll1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡢࡱࡪࡺࡡࡥࡣࡷࡥࠧᔦ")
    bstack1ll11l1llll_opy_ = bstack11ll1l_opy_ (u"ࠦࡵ࡫࡮ࡥ࡫ࡱ࡫ࠧᔧ")
    bstack1l1llll1l11_opy_ = bstack11ll1l_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨᔨ")
    bstack1l11l111l1l_opy_ = bstack11ll1l_opy_ (u"ࠨࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠣᔩ")
    bstack1l1llll111l_opy_ = bstack11ll1l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡒࡏࡈࠤᔪ")
    bstack1l111lllll1_opy_ = bstack11ll1l_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᔫ")
    bstack1lll1l1ll1l_opy_: Dict[str, bstack1lll1l11lll_opy_] = dict()
    bstack1l111111l1l_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll111l11l1_opy_: List[str]
    bstack1ll11ll1111_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll111l11l1_opy_: List[str],
        bstack1ll11ll1111_opy_: Dict[str, str],
        bstack1lll11l11l1_opy_: bstack1lll11l111l_opy_
    ):
        self.bstack1ll111l11l1_opy_ = bstack1ll111l11l1_opy_
        self.bstack1ll11ll1111_opy_ = bstack1ll11ll1111_opy_
        self.bstack1lll11l11l1_opy_ = bstack1lll11l11l1_opy_
    def track_event(
        self,
        context: bstack1ll1l1l11l1_opy_,
        test_framework_state: bstack1lll1l1l11l_opy_,
        test_hook_state: bstack1lll11lll1l_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࢂࠨᔬ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll11ll1l1l_opy_(
        self,
        instance: bstack1lll1l11lll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1ll1l1_opy_ = TestFramework.bstack1l1ll1l1l1l_opy_(bstack1lllllllll1_opy_)
        if not bstack1l1ll1ll1l1_opy_ in TestFramework.bstack1l111111l1l_opy_:
            return
        self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࢁࡽࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࡶࠦᔭ").format(len(TestFramework.bstack1l111111l1l_opy_[bstack1l1ll1ll1l1_opy_])))
        for callback in TestFramework.bstack1l111111l1l_opy_[bstack1l1ll1ll1l1_opy_]:
            try:
                callback(self, instance, bstack1lllllllll1_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack11ll1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠦᔮ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll1l1l11ll_opy_(self):
        return
    @abc.abstractmethod
    def bstack1l1lllll111_opy_(self, instance, bstack1lllllllll1_opy_):
        return
    @abc.abstractmethod
    def bstack1l1lllll1l1_opy_(self, instance, bstack1lllllllll1_opy_):
        return
    @staticmethod
    def bstack1ll111l1l11_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1ll11111_opy_.create_context(target)
        instance = TestFramework.bstack1lll1l1ll1l_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1111l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1l11ll_opy_(reverse=True) -> List[bstack1lll1l11lll_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll1l1ll1l_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lllll11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l111lll111_opy_(ctx: bstack1lll1l1l1ll_opy_, reverse=True) -> List[bstack1lll1l11lll_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll1l1ll1l_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lllll11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llllllll11_opy_(instance: bstack1lll1l11lll_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1l11lll_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll1l1lll_opy_(instance: bstack1lll1l11lll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11ll1l_opy_ (u"ࠧࡹࡥࡵࡡࡶࡸࡦࡺࡥ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡬ࡧࡼࡁࢀࢃࠠࡷࡣ࡯ࡹࡪࡃࡻࡾࠤᔯ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11ll1lll_opy_(instance: bstack1lll1l11lll_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack11ll1l_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢࡨࡲࡹࡸࡩࡦࡵࡀࡿࢂࠨᔰ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l11111l111_opy_(instance: bstack1lll1l1l11l_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11ll1l_opy_ (u"ࠢࡶࡲࡧࡥࡹ࡫࡟ࡴࡶࡤࡸࡪࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾࢁࠥࡱࡥࡺ࠿ࡾࢁࠥࡼࡡ࡭ࡷࡨࡁࢀࢃࠢᔱ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll111l1l11_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll111l1l11_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll111l111l_opy_(instance: bstack1lll1l11lll_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1l1lll1l1ll_opy_(instance: bstack1lll1l11lll_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1ll1l1l1l_opy_(bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_]):
        return bstack11ll1l_opy_ (u"ࠣ࠼ࠥᔲ").join((bstack1lll1l1l11l_opy_(bstack1lllllllll1_opy_[0]).name, bstack1lll11lll1l_opy_(bstack1lllllllll1_opy_[1]).name))
    @staticmethod
    def bstack1lllll111ll_opy_(bstack1lllllllll1_opy_: Tuple[bstack1lll1l1l11l_opy_, bstack1lll11lll1l_opy_], callback: Callable):
        bstack1l1ll1ll1l1_opy_ = TestFramework.bstack1l1ll1l1l1l_opy_(bstack1lllllllll1_opy_)
        TestFramework.logger.debug(bstack11ll1l_opy_ (u"ࠤࡶࡩࡹࡥࡨࡰࡱ࡮ࡣࡨࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡩࡱࡲ࡯ࡤࡸࡥࡨ࡫ࡶࡸࡷࡿ࡟࡬ࡧࡼࡁࢀࢃࠢᔳ").format(bstack1l1ll1ll1l1_opy_))
        if not bstack1l1ll1ll1l1_opy_ in TestFramework.bstack1l111111l1l_opy_:
            TestFramework.bstack1l111111l1l_opy_[bstack1l1ll1ll1l1_opy_] = []
        TestFramework.bstack1l111111l1l_opy_[bstack1l1ll1ll1l1_opy_].append(callback)
    @staticmethod
    def bstack1l1llll1l1l_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡵ࡫ࡱࡷࠧᔴ"):
            return klass.__qualname__
        return module + bstack11ll1l_opy_ (u"ࠦ࠳ࠨᔵ") + klass.__qualname__
    @staticmethod
    def bstack1ll111llll1_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}