# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll1l11111_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1ll1lll111l_opy_, bstack1lll1l1ll1l_opy_
class bstack1lll1llll11_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1ll1l_opy_ (u"࡙ࠦ࡫ࡳࡵࡊࡲࡳࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᓓ").format(self.name)
class bstack1llll11l1ll_opy_(Enum):
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
        return bstack1ll1l_opy_ (u"࡚ࠧࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᓔ").format(self.name)
class bstack1lll1l1l1ll_opy_(bstack1ll1lll111l_opy_):
    bstack1ll1ll111ll_opy_: List[str]
    bstack1l1llllll11_opy_: Dict[str, str]
    state: bstack1llll11l1ll_opy_
    bstack1lll111111l_opy_: datetime
    bstack1l1111l111l_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1l1ll1l_opy_,
        bstack1ll1ll111ll_opy_: List[str],
        bstack1l1llllll11_opy_: Dict[str, str],
        state=bstack1llll11l1ll_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll1ll111ll_opy_ = bstack1ll1ll111ll_opy_
        self.bstack1l1llllll11_opy_ = bstack1l1llllll11_opy_
        self.state = state
        self.bstack1lll111111l_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l111l_opy_ = datetime.now(tz=timezone.utc)
    def bstack1111111ll1_opy_(self, bstack1l1111l11l1_opy_: bstack1llll11l1ll_opy_):
        bstack1l1111l11ll_opy_ = bstack1llll11l1ll_opy_(bstack1l1111l11l1_opy_).name
        if not bstack1l1111l11ll_opy_:
            return False
        if bstack1l1111l11l1_opy_ == self.state:
            return False
        self.state = bstack1l1111l11l1_opy_
        self.bstack1l1111l111l_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll1l1lllll_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll11lll111_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll11ll11ll_opy_: int = None
    bstack1l1llllllll_opy_: str = None
    bstack1ll1ll_opy_: str = None
    bstack1lllll111l_opy_: str = None
    bstack1ll11llll1l_opy_: str = None
    bstack1ll11l11lll_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llll11ll1l_opy_ = bstack1ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡺࡻࡩࡥࠤᓕ")
    bstack1ll11l1llll_opy_ = bstack1ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡯ࡤࠣᓖ")
    bstack1ll1l11l11l_opy_ = bstack1ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡮ࡢ࡯ࡨࠦᓗ")
    bstack1ll1ll11111_opy_ = bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡤࡶࡡࡵࡪࠥᓘ")
    bstack1ll1l1lll11_opy_ = bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡶࡤ࡫ࡸࠨᓙ")
    bstack1lll1l11l1l_opy_ = bstack1ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡸࡻ࡬ࡵࠤᓚ")
    bstack1l1llllll1l_opy_ = bstack1ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡹࡵ࡭ࡶࡢࡥࡹࠨᓛ")
    bstack1ll11l11l11_opy_ = bstack1ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᓜ")
    bstack1ll11llllll_opy_ = bstack1ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᓝ")
    bstack1ll11111l11_opy_ = bstack1ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᓞ")
    bstack1llll11llll_opy_ = bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠣᓟ")
    bstack1lll1l11l11_opy_ = bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧᓠ")
    bstack1ll11l111l1_opy_ = bstack1ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡦࡳࡩ࡫ࠢᓡ")
    bstack1ll111l11ll_opy_ = bstack1ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠢᓢ")
    bstack1lllllllll1_opy_ = bstack1ll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࠢᓣ")
    bstack1llll1111ll_opy_ = bstack1ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡡࡪ࡮ࡸࡶࡪࠨᓤ")
    bstack1ll11llll11_opy_ = bstack1ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠧᓥ")
    bstack1ll1l11l111_opy_ = bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡭ࡱࡪࡷࠧᓦ")
    bstack1ll111llll1_opy_ = bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠ࡯ࡨࡸࡦࠨᓧ")
    bstack1l1111l1l11_opy_ = bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡶࡧࡴࡶࡥࡴࠩᓨ")
    bstack1lll111llll_opy_ = bstack1ll1l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨᓩ")
    bstack1ll1l111111_opy_ = bstack1ll1l_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᓪ")
    bstack1ll11111l1l_opy_ = bstack1ll1l_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡥ࡯ࡦࡨࡨࡤࡧࡴࠣᓫ")
    bstack1ll1l1ll1ll_opy_ = bstack1ll1l_opy_ (u"ࠣࡪࡲࡳࡰࡥࡩࡥࠤᓬ")
    bstack1ll11l111ll_opy_ = bstack1ll1l_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡳࡧࡶࡹࡱࡺࠢᓭ")
    bstack1ll11ll111l_opy_ = bstack1ll1l_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠ࡮ࡲ࡫ࡸࠨᓮ")
    bstack1ll11l1l111_opy_ = bstack1ll1l_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠢᓯ")
    bstack1ll111ll1ll_opy_ = bstack1ll1l_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᓰ")
    bstack1ll11ll11l1_opy_ = bstack1ll1l_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠣᓱ")
    bstack1ll111ll1l1_opy_ = bstack1ll1l_opy_ (u"ࠢࡱࡧࡱࡨ࡮ࡴࡧࠣᓲ")
    bstack1ll1l11l1ll_opy_ = bstack1ll1l_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤᓳ")
    bstack1l11ll1111l_opy_ = bstack1ll1l_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࠦᓴ")
    bstack1ll11l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡎࡒࡋࠧᓵ")
    bstack1l11l1llll1_opy_ = bstack1ll1l_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᓶ")
    bstack1lll1ll11ll_opy_: Dict[str, bstack1lll1l1l1ll_opy_] = dict()
    bstack1l1111l1l1l_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll1ll111ll_opy_: List[str]
    bstack1l1llllll11_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll1ll111ll_opy_: List[str],
        bstack1l1llllll11_opy_: Dict[str, str],
        bstack1lll11lllll_opy_: bstack1lll1l11111_opy_
    ):
        self.bstack1ll1ll111ll_opy_ = bstack1ll1ll111ll_opy_
        self.bstack1l1llllll11_opy_ = bstack1l1llllll11_opy_
        self.bstack1lll11lllll_opy_ = bstack1lll11lllll_opy_
    def track_event(
        self,
        context: bstack1ll1l1lllll_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1lll1llll11_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࢃࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠥࡧࡲࡨࡵࡀࡿࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻࡾࠤᓷ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1l1llll1lll_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1lllll_opy_ = TestFramework.bstack1l1llll1l1l_opy_(bstack1llllll111l_opy_)
        if not bstack1l1ll1lllll_opy_ in TestFramework.bstack1l1111l1l1l_opy_:
            return
        self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡽࢀࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡹࠢᓸ").format(len(TestFramework.bstack1l1111l1l1l_opy_[bstack1l1ll1lllll_opy_])))
        for callback in TestFramework.bstack1l1111l1l1l_opy_[bstack1l1ll1lllll_opy_]:
            try:
                callback(self, instance, bstack1llllll111l_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack1ll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠢᓹ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll11lll1ll_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll1l111l1l_opy_(self, instance, bstack1llllll111l_opy_):
        return
    @abc.abstractmethod
    def bstack1ll11l1lll1_opy_(self, instance, bstack1llllll111l_opy_):
        return
    @staticmethod
    def bstack1l1lllllll1_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1lll111l_opy_.create_context(target)
        instance = TestFramework.bstack1lll1ll11ll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1lll1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1lll1l_opy_(reverse=True) -> List[bstack1lll1l1l1ll_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll1ll11ll_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111111l_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11l11l11l_opy_(ctx: bstack1lll1l1ll1l_opy_, reverse=True) -> List[bstack1lll1l1l1ll_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll1ll11ll_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111111l_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllll11lll_opy_(instance: bstack1lll1l1l1ll_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1l1l1ll_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1111111ll1_opy_(instance: bstack1lll1l1l1ll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1ll1l_opy_ (u"ࠣࡵࡨࡸࡤࡹࡴࡢࡶࡨ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣ࡯ࡪࡿ࠽ࡼࡿࠣࡺࡦࡲࡵࡦ࠿ࡾࢁࠧᓺ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll1l1l11ll_opy_(instance: bstack1lll1l1l1ll_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack1ll1l_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩࡤ࡫࡮ࡵࡴ࡬ࡩࡸࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾࢁࠥ࡫࡮ࡵࡴ࡬ࡩࡸࡃࡻࡾࠤᓻ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l1111l1111_opy_(instance: bstack1llll11l1ll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1ll1l_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡽࠡ࡭ࡨࡽࡂࢁࡽࠡࡸࡤࡰࡺ࡫࠽ࡼࡿࠥᓼ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1l1lllllll1_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1l1lllllll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll1l1l1l11_opy_(instance: bstack1lll1l1l1ll_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1l1lllll1ll_opy_(instance: bstack1lll1l1l1ll_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1llll1l1l_opy_(bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_]):
        return bstack1ll1l_opy_ (u"ࠦ࠿ࠨᓽ").join((bstack1llll11l1ll_opy_(bstack1llllll111l_opy_[0]).name, bstack1lll1llll11_opy_(bstack1llllll111l_opy_[1]).name))
    @staticmethod
    def bstack1lllll1l11l_opy_(bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_], callback: Callable):
        bstack1l1ll1lllll_opy_ = TestFramework.bstack1l1llll1l1l_opy_(bstack1llllll111l_opy_)
        TestFramework.logger.debug(bstack1ll1l_opy_ (u"ࠧࡹࡥࡵࡡ࡫ࡳࡴࡱ࡟ࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣ࡬ࡴࡵ࡫ࡠࡴࡨ࡫࡮ࡹࡴࡳࡻࡢ࡯ࡪࡿ࠽ࡼࡿࠥᓾ").format(bstack1l1ll1lllll_opy_))
        if not bstack1l1ll1lllll_opy_ in TestFramework.bstack1l1111l1l1l_opy_:
            TestFramework.bstack1l1111l1l1l_opy_[bstack1l1ll1lllll_opy_] = []
        TestFramework.bstack1l1111l1l1l_opy_[bstack1l1ll1lllll_opy_].append(callback)
    @staticmethod
    def bstack1ll11l1ll11_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡸ࡮ࡴࡳࠣᓿ"):
            return klass.__qualname__
        return module + bstack1ll1l_opy_ (u"ࠢ࠯ࠤᔀ") + klass.__qualname__
    @staticmethod
    def bstack1ll111lll1l_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}