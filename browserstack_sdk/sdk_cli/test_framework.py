# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111111_opy_ import bstack1ll1lll1111_opy_, bstack1lll1l1111l_opy_
class bstack1lll1lll11l_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack111111l_opy_ (u"ࠨࡔࡦࡵࡷࡌࡴࡵ࡫ࡔࡶࡤࡸࡪ࠴ࡻࡾࠤᓎ").format(self.name)
class bstack1llll111lll_opy_(Enum):
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
        return bstack111111l_opy_ (u"ࠢࡕࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡣࡷࡩ࠳ࢁࡽࠣᓏ").format(self.name)
class bstack1lll1lll1l1_opy_(bstack1ll1lll1111_opy_):
    bstack1ll11l11ll1_opy_: List[str]
    bstack1ll11lll11l_opy_: Dict[str, str]
    state: bstack1llll111lll_opy_
    bstack1lll111l1l1_opy_: datetime
    bstack1l1111l11ll_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1l1111l_opy_,
        bstack1ll11l11ll1_opy_: List[str],
        bstack1ll11lll11l_opy_: Dict[str, str],
        state=bstack1llll111lll_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll11l11ll1_opy_ = bstack1ll11l11ll1_opy_
        self.bstack1ll11lll11l_opy_ = bstack1ll11lll11l_opy_
        self.state = state
        self.bstack1lll111l1l1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll1lll1l_opy_(self, bstack1l1111l11l1_opy_: bstack1llll111lll_opy_):
        bstack1l1111l1111_opy_ = bstack1llll111lll_opy_(bstack1l1111l11l1_opy_).name
        if not bstack1l1111l1111_opy_:
            return False
        if bstack1l1111l11l1_opy_ == self.state:
            return False
        self.state = bstack1l1111l11l1_opy_
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1l1llllllll_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll111lll11_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll11l1ll11_opy_: int = None
    bstack1ll1l1l1l11_opy_: str = None
    bstack1111l1l_opy_: str = None
    bstack11lll1l1ll_opy_: str = None
    bstack1ll1ll111l1_opy_: str = None
    bstack1ll1l1l1ll1_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llll11lll1_opy_ = bstack111111l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠦᓐ")
    bstack1ll1l11l11l_opy_ = bstack111111l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡪࡦࠥᓑ")
    bstack1ll11lll111_opy_ = bstack111111l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡰࡤࡱࡪࠨᓒ")
    bstack1ll11111l1l_opy_ = bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫࡟ࡱࡣࡷ࡬ࠧᓓ")
    bstack1ll11lll1ll_opy_ = bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡸࡦ࡭ࡳࠣᓔ")
    bstack1lll1ll1ll1_opy_ = bstack111111l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦᓕ")
    bstack1ll1l1111ll_opy_ = bstack111111l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡥࡴࡷ࡯ࡸࡤࡧࡴࠣᓖ")
    bstack1ll111l1l11_opy_ = bstack111111l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᓗ")
    bstack1ll11l1l1ll_opy_ = bstack111111l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡦࡰࡧࡩࡩࡥࡡࡵࠤᓘ")
    bstack1ll111l1lll_opy_ = bstack111111l_opy_ (u"ࠥࡸࡪࡹࡴࡠ࡮ࡲࡧࡦࡺࡩࡰࡰࠥᓙ")
    bstack1llll1111l1_opy_ = bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࠥᓚ")
    bstack1llll1l11l1_opy_ = bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠢᓛ")
    bstack1ll1111llll_opy_ = bstack111111l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡨࡵࡤࡦࠤᓜ")
    bstack1ll11ll11l1_opy_ = bstack111111l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠤᓝ")
    bstack1llllllll1l_opy_ = bstack111111l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࠤᓞ")
    bstack1lll1ll11ll_opy_ = bstack111111l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡣ࡬ࡰࡺࡸࡥࠣᓟ")
    bstack1ll111ll111_opy_ = bstack111111l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠢᓠ")
    bstack1ll1ll11l11_opy_ = bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡯ࡳ࡬ࡹࠢᓡ")
    bstack1ll1l1lllll_opy_ = bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡱࡪࡺࡡࠣᓢ")
    bstack1l1111l1l1l_opy_ = bstack111111l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡸࡩ࡯ࡱࡧࡶࠫᓣ")
    bstack1lll11ll1l1_opy_ = bstack111111l_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࡡࡶࡩࡸࡹࡩࡰࡰࡢࡲࡦࡳࡥࠣᓤ")
    bstack1ll11lllll1_opy_ = bstack111111l_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠦᓥ")
    bstack1ll111ll1ll_opy_ = bstack111111l_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡧࡱࡨࡪࡪ࡟ࡢࡶࠥᓦ")
    bstack1ll1l1111l1_opy_ = bstack111111l_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠ࡫ࡧࠦᓧ")
    bstack1ll11l111ll_opy_ = bstack111111l_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡࡵࡩࡸࡻ࡬ࡵࠤᓨ")
    bstack1ll11l1l1l1_opy_ = bstack111111l_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢࡰࡴ࡭ࡳࠣᓩ")
    bstack1ll11l1l111_opy_ = bstack111111l_opy_ (u"ࠨࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠤᓪ")
    bstack1ll11l11l1l_opy_ = bstack111111l_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᓫ")
    bstack1ll1l1ll1l1_opy_ = bstack111111l_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡠ࡯ࡨࡸࡦࡪࡡࡵࡣࠥᓬ")
    bstack1ll11llll1l_opy_ = bstack111111l_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥᓭ")
    bstack1ll11ll1l11_opy_ = bstack111111l_opy_ (u"ࠥࡴࡪࡴࡤࡪࡰࡪࠦᓮ")
    bstack1l11l1l1ll1_opy_ = bstack111111l_opy_ (u"࡙ࠦࡋࡓࡕࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙ࠨᓯ")
    bstack1ll1l1l11l1_opy_ = bstack111111l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡐࡔࡍࠢᓰ")
    bstack1l11l11l1l1_opy_ = bstack111111l_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᓱ")
    bstack1llll111l1l_opy_: Dict[str, bstack1lll1lll1l1_opy_] = dict()
    bstack1l1111l1l11_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll11l11ll1_opy_: List[str]
    bstack1ll11lll11l_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll11l11ll1_opy_: List[str],
        bstack1ll11lll11l_opy_: Dict[str, str],
        bstack1lll11lllll_opy_: bstack1lll11llll1_opy_
    ):
        self.bstack1ll11l11ll1_opy_ = bstack1ll11l11ll1_opy_
        self.bstack1ll11lll11l_opy_ = bstack1ll11lll11l_opy_
        self.bstack1lll11lllll_opy_ = bstack1lll11lllll_opy_
    def track_event(
        self,
        context: bstack1l1llllllll_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack111111l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࢃࠠࡢࡴࡪࡷࡂࢁࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽࢀࠦᓲ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll1l11l1l1_opy_(
        self,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1lll1l1l1_opy_ = TestFramework.bstack1l1lll11lll_opy_(bstack1lllll1l1ll_opy_)
        if not bstack1l1lll1l1l1_opy_ in TestFramework.bstack1l1111l1l11_opy_:
            return
        self.logger.debug(bstack111111l_opy_ (u"ࠣ࡫ࡱࡺࡴࡱࡩ࡯ࡩࠣࡿࢂࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࡴࠤᓳ").format(len(TestFramework.bstack1l1111l1l11_opy_[bstack1l1lll1l1l1_opy_])))
        for callback in TestFramework.bstack1l1111l1l11_opy_[bstack1l1lll1l1l1_opy_]:
            try:
                callback(self, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack111111l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠡ࡫ࡱࡺࡴࡱࡩ࡯ࡩࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠤᓴ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll1l1lll11_opy_(self):
        return
    @abc.abstractmethod
    def bstack1l1lllll11l_opy_(self, instance, bstack1lllll1l1ll_opy_):
        return
    @abc.abstractmethod
    def bstack1l1llll1lll_opy_(self, instance, bstack1lllll1l1ll_opy_):
        return
    @staticmethod
    def bstack1ll11ll1lll_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1lll1111_opy_.create_context(target)
        instance = TestFramework.bstack1llll111l1l_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1llll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l11l1ll_opy_(reverse=True) -> List[bstack1lll1lll1l1_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1llll111l1l_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111l1l1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11l1111l1_opy_(ctx: bstack1lll1l1111l_opy_, reverse=True) -> List[bstack1lll1lll1l1_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1llll111l1l_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111l1l1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllllll11l_opy_(instance: bstack1lll1lll1l1_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1lll1l1_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll1lll1l_opy_(instance: bstack1lll1lll1l1_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack111111l_opy_ (u"ࠥࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾࢁࠥࡱࡥࡺ࠿ࡾࢁࠥࡼࡡ࡭ࡷࡨࡁࢀࢃࠢᓵ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll1l11l111_opy_(instance: bstack1lll1lll1l1_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack111111l_opy_ (u"ࠦࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࡟ࡦࡰࡷࡶ࡮࡫ࡳ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠࡦࡰࡷࡶ࡮࡫ࡳ࠾ࡽࢀࠦᓶ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l1111l111l_opy_(instance: bstack1llll111lll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack111111l_opy_ (u"ࠧࡻࡰࡥࡣࡷࡩࡤࡹࡴࡢࡶࡨ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣ࡯ࡪࡿ࠽ࡼࡿࠣࡺࡦࡲࡵࡦ࠿ࡾࢁࠧᓷ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll11ll1lll_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll11ll1lll_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll111l1111_opy_(instance: bstack1lll1lll1l1_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll111lll1l_opy_(instance: bstack1lll1lll1l1_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1lll11lll_opy_(bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_]):
        return bstack111111l_opy_ (u"ࠨ࠺ࠣᓸ").join((bstack1llll111lll_opy_(bstack1lllll1l1ll_opy_[0]).name, bstack1lll1lll11l_opy_(bstack1lllll1l1ll_opy_[1]).name))
    @staticmethod
    def bstack1111111l11_opy_(bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_], callback: Callable):
        bstack1l1lll1l1l1_opy_ = TestFramework.bstack1l1lll11lll_opy_(bstack1lllll1l1ll_opy_)
        TestFramework.logger.debug(bstack111111l_opy_ (u"ࠢࡴࡧࡷࡣ࡭ࡵ࡯࡬ࡡࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥ࡮࡯ࡰ࡭ࡢࡶࡪ࡭ࡩࡴࡶࡵࡽࡤࡱࡥࡺ࠿ࡾࢁࠧᓹ").format(bstack1l1lll1l1l1_opy_))
        if not bstack1l1lll1l1l1_opy_ in TestFramework.bstack1l1111l1l11_opy_:
            TestFramework.bstack1l1111l1l11_opy_[bstack1l1lll1l1l1_opy_] = []
        TestFramework.bstack1l1111l1l11_opy_[bstack1l1lll1l1l1_opy_].append(callback)
    @staticmethod
    def bstack1ll1l1ll11l_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡺࡩ࡯ࡵࠥᓺ"):
            return klass.__qualname__
        return module + bstack111111l_opy_ (u"ࠤ࠱ࠦᓻ") + klass.__qualname__
    @staticmethod
    def bstack1ll11111l11_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}