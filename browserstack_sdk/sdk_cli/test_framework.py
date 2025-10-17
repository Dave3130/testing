# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll11lll11_opy_ import bstack1lll11ll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111l11_opy_ import bstack1ll1ll1ll1l_opy_, bstack1lll1lll1l1_opy_
class bstack1lll1ll11ll_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l111_opy_ (u"ࠢࡕࡧࡶࡸࡍࡵ࡯࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥᓈ").format(self.name)
class bstack1lll1l1l1ll_opy_(Enum):
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
        return bstack11l111_opy_ (u"ࠣࡖࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡔࡶࡤࡸࡪ࠴ࡻࡾࠤᓉ").format(self.name)
class bstack1lll1ll1lll_opy_(bstack1ll1ll1ll1l_opy_):
    bstack1ll111ll1ll_opy_: List[str]
    bstack1l1llllll11_opy_: Dict[str, str]
    state: bstack1lll1l1l1ll_opy_
    bstack1ll1llllll1_opy_: datetime
    bstack1l1111l11ll_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1lll1l1_opy_,
        bstack1ll111ll1ll_opy_: List[str],
        bstack1l1llllll11_opy_: Dict[str, str],
        state=bstack1lll1l1l1ll_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll111ll1ll_opy_ = bstack1ll111ll1ll_opy_
        self.bstack1l1llllll11_opy_ = bstack1l1llllll11_opy_
        self.state = state
        self.bstack1ll1llllll1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll111ll_opy_(self, bstack1l1111l1111_opy_: bstack1lll1l1l1ll_opy_):
        bstack1l1111l11l1_opy_ = bstack1lll1l1l1ll_opy_(bstack1l1111l1111_opy_).name
        if not bstack1l1111l11l1_opy_:
            return False
        if bstack1l1111l1111_opy_ == self.state:
            return False
        self.state = bstack1l1111l1111_opy_
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll1111l11l_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll1111lll1_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll11l11lll_opy_: int = None
    bstack1ll1l1111l1_opy_: str = None
    bstack11ll11_opy_: str = None
    bstack1111ll1l1_opy_: str = None
    bstack1ll11ll1l11_opy_: str = None
    bstack1ll1111l111_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1l111l1_opy_ = bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠧᓊ")
    bstack1l1llll1ll1_opy_ = bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡠ࡫ࡧࠦᓋ")
    bstack1ll11l111ll_opy_ = bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡱࡥࡲ࡫ࠢᓌ")
    bstack1ll111l11ll_opy_ = bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡠࡲࡤࡸ࡭ࠨᓍ")
    bstack1l1llll1lll_opy_ = bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡹࡧࡧࡴࠤᓎ")
    bstack1llll1111l1_opy_ = bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡥࡴࡷ࡯ࡸࠧᓏ")
    bstack1l1lllll1l1_opy_ = bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡦࡵࡸࡰࡹࡥࡡࡵࠤᓐ")
    bstack1ll11l11l1l_opy_ = bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠦᓑ")
    bstack1ll11ll111l_opy_ = bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡧࡱࡨࡪࡪ࡟ࡢࡶࠥᓒ")
    bstack1ll1l1ll11l_opy_ = bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡯ࡳࡨࡧࡴࡪࡱࡱࠦᓓ")
    bstack1lll1llll1l_opy_ = bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࠦᓔ")
    bstack1llll111lll_opy_ = bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣᓕ")
    bstack1ll1l111lll_opy_ = bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡤࡩ࡯ࡥࡧࠥᓖ")
    bstack1ll11ll1lll_opy_ = bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡦࡴࡸࡲࡤࡴࡡ࡮ࡧࠥᓗ")
    bstack1111111l1l_opy_ = bstack11l111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࠥᓘ")
    bstack1llll11llll_opy_ = bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨࡤ࡭ࡱࡻࡲࡦࠤᓙ")
    bstack1ll111111l1_opy_ = bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠣᓚ")
    bstack1l1llllllll_opy_ = bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡰࡴ࡭ࡳࠣᓛ")
    bstack1ll1l1ll111_opy_ = bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡲ࡫ࡴࡢࠤᓜ")
    bstack1l11111lll1_opy_ = bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡹࡣࡰࡲࡨࡷࠬᓝ")
    bstack1lll111llll_opy_ = bstack11l111_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤᓞ")
    bstack1ll1l11llll_opy_ = bstack11l111_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᓟ")
    bstack1l1lllllll1_opy_ = bstack11l111_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡨࡲࡩ࡫ࡤࡠࡣࡷࠦᓠ")
    bstack1ll1l1l11l1_opy_ = bstack11l111_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡ࡬ࡨࠧᓡ")
    bstack1ll1l1l1lll_opy_ = bstack11l111_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢࡶࡪࡹࡵ࡭ࡶࠥᓢ")
    bstack1ll11lll1ll_opy_ = bstack11l111_opy_ (u"ࠨࡨࡰࡱ࡮ࡣࡱࡵࡧࡴࠤᓣ")
    bstack1ll1l111ll1_opy_ = bstack11l111_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠥᓤ")
    bstack1ll1111llll_opy_ = bstack11l111_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᓥ")
    bstack1ll1111l1ll_opy_ = bstack11l111_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡡࡰࡩࡹࡧࡤࡢࡶࡤࠦᓦ")
    bstack1ll11llllll_opy_ = bstack11l111_opy_ (u"ࠥࡴࡪࡴࡤࡪࡰࡪࠦᓧ")
    bstack1ll1l1lllll_opy_ = bstack11l111_opy_ (u"ࠦࡵ࡫࡮ࡥ࡫ࡱ࡫ࠧᓨ")
    bstack1l11l11ll1l_opy_ = bstack11l111_opy_ (u"࡚ࠧࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠢᓩ")
    bstack1ll1l1l1111_opy_ = bstack11l111_opy_ (u"ࠨࡔࡆࡕࡗࡣࡑࡕࡇࠣᓪ")
    bstack1l11l1ll1ll_opy_ = bstack11l111_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᓫ")
    bstack1lll1l11lll_opy_: Dict[str, bstack1lll1ll1lll_opy_] = dict()
    bstack1l1111l111l_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll111ll1ll_opy_: List[str]
    bstack1l1llllll11_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll111ll1ll_opy_: List[str],
        bstack1l1llllll11_opy_: Dict[str, str],
        bstack1lll11lll11_opy_: bstack1lll11ll1ll_opy_
    ):
        self.bstack1ll111ll1ll_opy_ = bstack1ll111ll1ll_opy_
        self.bstack1l1llllll11_opy_ = bstack1l1llllll11_opy_
        self.bstack1lll11lll11_opy_ = bstack1lll11lll11_opy_
    def track_event(
        self,
        context: bstack1ll1111l11l_opy_,
        test_framework_state: bstack1lll1l1l1ll_opy_,
        test_hook_state: bstack1lll1ll11ll_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack11l111_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡿࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁࡽࠡࡣࡵ࡫ࡸࡃࡻࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾࢁࠧᓬ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll111ll1l1_opy_(
        self,
        instance: bstack1lll1ll1lll_opy_,
        bstack1llll1ll1ll_opy_: Tuple[bstack1lll1l1l1ll_opy_, bstack1lll1ll11ll_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1lll1llll_opy_ = TestFramework.bstack1l1lll11ll1_opy_(bstack1llll1ll1ll_opy_)
        if not bstack1l1lll1llll_opy_ in TestFramework.bstack1l1111l111l_opy_:
            return
        self.logger.debug(bstack11l111_opy_ (u"ࠤ࡬ࡲࡻࡵ࡫ࡪࡰࡪࠤࢀࢃࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬ࡵࠥᓭ").format(len(TestFramework.bstack1l1111l111l_opy_[bstack1l1lll1llll_opy_])))
        for callback in TestFramework.bstack1l1111l111l_opy_[bstack1l1lll1llll_opy_]:
            try:
                callback(self, instance, bstack1llll1ll1ll_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack11l111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠢ࡬ࡲࡻࡵ࡫ࡪࡰࡪࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠥᓮ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll1l1l1l11_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll111l1lll_opy_(self, instance, bstack1llll1ll1ll_opy_):
        return
    @abc.abstractmethod
    def bstack1l1lllll11l_opy_(self, instance, bstack1llll1ll1ll_opy_):
        return
    @staticmethod
    def bstack1ll111llll1_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1ll1ll1l_opy_.create_context(target)
        instance = TestFramework.bstack1lll1l11lll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1l1ll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l111lll_opy_(reverse=True) -> List[bstack1lll1ll1lll_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll1l11lll_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1llllll1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11l11l1ll_opy_(ctx: bstack1lll1lll1l1_opy_, reverse=True) -> List[bstack1lll1ll1lll_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll1l11lll_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1llllll1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllll11l1l_opy_(instance: bstack1lll1ll1lll_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1ll1lll_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll111ll_opy_(instance: bstack1lll1ll1lll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l111_opy_ (u"ࠦࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿࢂࠦ࡫ࡦࡻࡀࡿࢂࠦࡶࡢ࡮ࡸࡩࡂࢁࡽࠣᓯ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll1l1lll1l_opy_(instance: bstack1lll1ll1lll_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack11l111_opy_ (u"ࠧࡹࡥࡵࡡࡶࡸࡦࡺࡥࡠࡧࡱࡸࡷ࡯ࡥࡴ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡽࠡࡧࡱࡸࡷ࡯ࡥࡴ࠿ࡾࢁࠧᓰ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l11111llll_opy_(instance: bstack1lll1l1l1ll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l111_opy_ (u"ࠨࡵࡱࡦࡤࡸࡪࡥࡳࡵࡣࡷࡩ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽࢀࠤࡰ࡫ࡹ࠾ࡽࢀࠤࡻࡧ࡬ࡶࡧࡀࡿࢂࠨᓱ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll111llll1_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll111llll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11lllll1_opy_(instance: bstack1lll1ll1lll_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll11l111l1_opy_(instance: bstack1lll1ll1lll_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1lll11ll1_opy_(bstack1llll1ll1ll_opy_: Tuple[bstack1lll1l1l1ll_opy_, bstack1lll1ll11ll_opy_]):
        return bstack11l111_opy_ (u"ࠢ࠻ࠤᓲ").join((bstack1lll1l1l1ll_opy_(bstack1llll1ll1ll_opy_[0]).name, bstack1lll1ll11ll_opy_(bstack1llll1ll1ll_opy_[1]).name))
    @staticmethod
    def bstack1llll1llll1_opy_(bstack1llll1ll1ll_opy_: Tuple[bstack1lll1l1l1ll_opy_, bstack1lll1ll11ll_opy_], callback: Callable):
        bstack1l1lll1llll_opy_ = TestFramework.bstack1l1lll11ll1_opy_(bstack1llll1ll1ll_opy_)
        TestFramework.logger.debug(bstack11l111_opy_ (u"ࠣࡵࡨࡸࡤ࡮࡯ࡰ࡭ࡢࡧࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡨࡰࡱ࡮ࡣࡷ࡫ࡧࡪࡵࡷࡶࡾࡥ࡫ࡦࡻࡀࡿࢂࠨᓳ").format(bstack1l1lll1llll_opy_))
        if not bstack1l1lll1llll_opy_ in TestFramework.bstack1l1111l111l_opy_:
            TestFramework.bstack1l1111l111l_opy_[bstack1l1lll1llll_opy_] = []
        TestFramework.bstack1l1111l111l_opy_[bstack1l1lll1llll_opy_].append(callback)
    @staticmethod
    def bstack1ll1l1111ll_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡴࡪࡰࡶࠦᓴ"):
            return klass.__qualname__
        return module + bstack11l111_opy_ (u"ࠥ࠲ࠧᓵ") + klass.__qualname__
    @staticmethod
    def bstack1l1lllll111_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}