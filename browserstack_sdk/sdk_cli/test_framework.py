# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l1111_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1ll11111_opy_, bstack1lll1l1l1ll_opy_
class bstack1lll1l1llll_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l11ll_opy_ (u"ࠣࡖࡨࡷࡹࡎ࡯ࡰ࡭ࡖࡸࡦࡺࡥ࠯ࡽࢀࠦᔈ").format(self.name)
class bstack1lll1ll11l1_opy_(Enum):
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
        return bstack11l11ll_opy_ (u"ࠤࡗࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥᔉ").format(self.name)
class bstack1lll1l1l11l_opy_(bstack1ll1ll11111_opy_):
    bstack1ll11ll1l1l_opy_: List[str]
    bstack1ll11l1l111_opy_: Dict[str, str]
    state: bstack1lll1ll11l1_opy_
    bstack1ll1lll1l11_opy_: datetime
    bstack1l1111111ll_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1l1l1ll_opy_,
        bstack1ll11ll1l1l_opy_: List[str],
        bstack1ll11l1l111_opy_: Dict[str, str],
        state=bstack1lll1ll11l1_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll11ll1l1l_opy_ = bstack1ll11ll1l1l_opy_
        self.bstack1ll11l1l111_opy_ = bstack1ll11l1l111_opy_
        self.state = state
        self.bstack1ll1lll1l11_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111111ll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll1l1l11_opy_(self, bstack1l11111l111_opy_: bstack1lll1ll11l1_opy_):
        bstack1l111111l11_opy_ = bstack1lll1ll11l1_opy_(bstack1l11111l111_opy_).name
        if not bstack1l111111l11_opy_:
            return False
        if bstack1l11111l111_opy_ == self.state:
            return False
        self.state = bstack1l11111l111_opy_
        self.bstack1l1111111ll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1l1llll111l_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll1l1l1l11_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll1l11ll11_opy_: int = None
    bstack1ll1l11l1l1_opy_: str = None
    bstack11lll1_opy_: str = None
    bstack1l1ll11l1l_opy_: str = None
    bstack1ll1111lll1_opy_: str = None
    bstack1ll11lll1ll_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll11l1lll_opy_ = bstack11l11ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡷࡸ࡭ࡩࠨᔊ")
    bstack1ll1l111l1l_opy_ = bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡬ࡨࠧᔋ")
    bstack1l1lll1llll_opy_ = bstack11l11ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡲࡦࡳࡥࠣᔌ")
    bstack1ll111llll1_opy_ = bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡡࡳࡥࡹ࡮ࠢᔍ")
    bstack1ll111l1ll1_opy_ = bstack11l11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡺࡡࡨࡵࠥᔎ")
    bstack1lll11l1l11_opy_ = bstack11l11ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡦࡵࡸࡰࡹࠨᔏ")
    bstack1l1lllll1ll_opy_ = bstack11l11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡶࡹࡱࡺ࡟ࡢࡶࠥᔐ")
    bstack1ll11lll1l1_opy_ = bstack11l11ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᔑ")
    bstack1ll11ll11l1_opy_ = bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡨࡲࡩ࡫ࡤࡠࡣࡷࠦᔒ")
    bstack1ll11l111l1_opy_ = bstack11l11ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡰࡴࡩࡡࡵ࡫ࡲࡲࠧᔓ")
    bstack1llll11111l_opy_ = bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠧᔔ")
    bstack1lll11l1ll1_opy_ = bstack11l11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤᔕ")
    bstack1ll11llllll_opy_ = bstack11l11ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡣࡰࡦࡨࠦᔖ")
    bstack1ll1l11111l_opy_ = bstack11l11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠦᔗ")
    bstack1llll1lll11_opy_ = bstack11l11ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠦᔘ")
    bstack1lll1l1l1l1_opy_ = bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩࡥ࡮ࡲࡵࡳࡧࠥᔙ")
    bstack1l1lll1l1ll_opy_ = bstack11l11ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠤᔚ")
    bstack1ll11l1l11l_opy_ = bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡣࡱࡵࡧࡴࠤᔛ")
    bstack1ll1l111lll_opy_ = bstack11l11ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡳࡥࡵࡣࠥᔜ")
    bstack1l111111l1l_opy_ = bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡳࡤࡱࡳࡩࡸ࠭ᔝ")
    bstack1lll111llll_opy_ = bstack11l11ll_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᔞ")
    bstack1ll1l11ll1l_opy_ = bstack11l11ll_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᔟ")
    bstack1l1lll1ll11_opy_ = bstack11l11ll_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡩࡳࡪࡥࡥࡡࡤࡸࠧᔠ")
    bstack1ll11llll11_opy_ = bstack11l11ll_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢ࡭ࡩࠨᔡ")
    bstack1ll11l1lll1_opy_ = bstack11l11ll_opy_ (u"ࠨࡨࡰࡱ࡮ࡣࡷ࡫ࡳࡶ࡮ࡷࠦᔢ")
    bstack1l1llll1l11_opy_ = bstack11l11ll_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡲ࡯ࡨࡵࠥᔣ")
    bstack1l1lll1l111_opy_ = bstack11l11ll_opy_ (u"ࠣࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠦᔤ")
    bstack1ll1l1l111l_opy_ = bstack11l11ll_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᔥ")
    bstack1ll1l1l1l1l_opy_ = bstack11l11ll_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡢࡱࡪࡺࡡࡥࡣࡷࡥࠧᔦ")
    bstack1ll1111l1l1_opy_ = bstack11l11ll_opy_ (u"ࠦࡵ࡫࡮ࡥ࡫ࡱ࡫ࠧᔧ")
    bstack1l1lllll1l1_opy_ = bstack11l11ll_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨᔨ")
    bstack1l111lll11l_opy_ = bstack11l11ll_opy_ (u"ࠨࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠣᔩ")
    bstack1ll111l1111_opy_ = bstack11l11ll_opy_ (u"ࠢࡕࡇࡖࡘࡤࡒࡏࡈࠤᔪ")
    bstack1l11l11lll1_opy_ = bstack11l11ll_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᔫ")
    bstack1lll11l11ll_opy_: Dict[str, bstack1lll1l1l11l_opy_] = dict()
    bstack1l111111lll_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll11ll1l1l_opy_: List[str]
    bstack1ll11l1l111_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll11ll1l1l_opy_: List[str],
        bstack1ll11l1l111_opy_: Dict[str, str],
        bstack1lll11l11l1_opy_: bstack1lll11l1111_opy_
    ):
        self.bstack1ll11ll1l1l_opy_ = bstack1ll11ll1l1l_opy_
        self.bstack1ll11l1l111_opy_ = bstack1ll11l1l111_opy_
        self.bstack1lll11l11l1_opy_ = bstack1lll11l11l1_opy_
    def track_event(
        self,
        context: bstack1l1llll111l_opy_,
        test_framework_state: bstack1lll1ll11l1_opy_,
        test_hook_state: bstack1lll1l1llll_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack11l11ll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࢂࠨᔬ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll1l1l1111_opy_(
        self,
        instance: bstack1lll1l1l11l_opy_,
        bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1l111l_opy_ = TestFramework.bstack1l1lll11111_opy_(bstack1llll1ll1l1_opy_)
        if not bstack1l1ll1l111l_opy_ in TestFramework.bstack1l111111lll_opy_:
            return
        self.logger.debug(bstack11l11ll_opy_ (u"ࠥ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࢁࡽࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࡶࠦᔭ").format(len(TestFramework.bstack1l111111lll_opy_[bstack1l1ll1l111l_opy_])))
        for callback in TestFramework.bstack1l111111lll_opy_[bstack1l1ll1l111l_opy_]:
            try:
                callback(self, instance, bstack1llll1ll1l1_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack11l11ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠦᔮ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll111lll1l_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll11lll111_opy_(self, instance, bstack1llll1ll1l1_opy_):
        return
    @abc.abstractmethod
    def bstack1ll11ll11ll_opy_(self, instance, bstack1llll1ll1l1_opy_):
        return
    @staticmethod
    def bstack1ll11l11ll1_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1ll11111_opy_.create_context(target)
        instance = TestFramework.bstack1lll11l11ll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll111l1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l111ll1lll_opy_(reverse=True) -> List[bstack1lll1l1l11l_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll11l11ll_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lll1l11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11l1l1111_opy_(ctx: bstack1lll1l1l1ll_opy_, reverse=True) -> List[bstack1lll1l1l11l_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll11l11ll_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lll1l11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llllll11l1_opy_(instance: bstack1lll1l1l11l_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1l1l11l_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll1l1l11_opy_(instance: bstack1lll1l1l11l_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l11ll_opy_ (u"ࠧࡹࡥࡵࡡࡶࡸࡦࡺࡥ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡬ࡧࡼࡁࢀࢃࠠࡷࡣ࡯ࡹࡪࡃࡻࡾࠤᔯ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11ll1111_opy_(instance: bstack1lll1l1l11l_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack11l11ll_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢࡨࡲࡹࡸࡩࡦࡵࡀࡿࢂࠨᔰ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l111111ll1_opy_(instance: bstack1lll1ll11l1_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l11ll_opy_ (u"ࠢࡶࡲࡧࡥࡹ࡫࡟ࡴࡶࡤࡸࡪࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾࢁࠥࡱࡥࡺ࠿ࡾࢁࠥࡼࡡ࡭ࡷࡨࡁࢀࢃࠢᔱ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll11l11ll1_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll11l11ll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll111l11ll_opy_(instance: bstack1lll1l1l11l_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll111l1lll_opy_(instance: bstack1lll1l1l11l_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1lll11111_opy_(bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_]):
        return bstack11l11ll_opy_ (u"ࠣ࠼ࠥᔲ").join((bstack1lll1ll11l1_opy_(bstack1llll1ll1l1_opy_[0]).name, bstack1lll1l1llll_opy_(bstack1llll1ll1l1_opy_[1]).name))
    @staticmethod
    def bstack1llllll1l1l_opy_(bstack1llll1ll1l1_opy_: Tuple[bstack1lll1ll11l1_opy_, bstack1lll1l1llll_opy_], callback: Callable):
        bstack1l1ll1l111l_opy_ = TestFramework.bstack1l1lll11111_opy_(bstack1llll1ll1l1_opy_)
        TestFramework.logger.debug(bstack11l11ll_opy_ (u"ࠤࡶࡩࡹࡥࡨࡰࡱ࡮ࡣࡨࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡩࡱࡲ࡯ࡤࡸࡥࡨ࡫ࡶࡸࡷࡿ࡟࡬ࡧࡼࡁࢀࢃࠢᔳ").format(bstack1l1ll1l111l_opy_))
        if not bstack1l1ll1l111l_opy_ in TestFramework.bstack1l111111lll_opy_:
            TestFramework.bstack1l111111lll_opy_[bstack1l1ll1l111l_opy_] = []
        TestFramework.bstack1l111111lll_opy_[bstack1l1ll1l111l_opy_].append(callback)
    @staticmethod
    def bstack1ll11l11l11_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡵ࡫ࡱࡷࠧᔴ"):
            return klass.__qualname__
        return module + bstack11l11ll_opy_ (u"ࠦ࠳ࠨᔵ") + klass.__qualname__
    @staticmethod
    def bstack1ll11111111_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}