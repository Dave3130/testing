# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll11lllll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1ll1lll1111_opy_, bstack1lll1l11l11_opy_
class bstack1llll1l11l1_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1ll1ll1_opy_ (u"࡙ࠦ࡫ࡳࡵࡊࡲࡳࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᓚ").format(self.name)
class bstack1lll1l11lll_opy_(Enum):
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
        return bstack1ll1ll1_opy_ (u"࡚ࠧࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᓛ").format(self.name)
class bstack1llll1l1111_opy_(bstack1ll1lll1111_opy_):
    bstack1ll11111l1l_opy_: List[str]
    bstack1ll111l1l11_opy_: Dict[str, str]
    state: bstack1lll1l11lll_opy_
    bstack1lll11111ll_opy_: datetime
    bstack1l1111l11ll_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1l11l11_opy_,
        bstack1ll11111l1l_opy_: List[str],
        bstack1ll111l1l11_opy_: Dict[str, str],
        state=bstack1lll1l11lll_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll11111l1l_opy_ = bstack1ll11111l1l_opy_
        self.bstack1ll111l1l11_opy_ = bstack1ll111l1l11_opy_
        self.state = state
        self.bstack1lll11111ll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll1l1ll_opy_(self, bstack1l1111l1lll_opy_: bstack1lll1l11lll_opy_):
        bstack1l1111l11l1_opy_ = bstack1lll1l11lll_opy_(bstack1l1111l1lll_opy_).name
        if not bstack1l1111l11l1_opy_:
            return False
        if bstack1l1111l1lll_opy_ == self.state:
            return False
        self.state = bstack1l1111l1lll_opy_
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll1l1ll1ll_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll11l1l11l_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll11l1ll11_opy_: int = None
    bstack1ll1111lll1_opy_: str = None
    bstack1l1111l_opy_: str = None
    bstack1l1l11111l_opy_: str = None
    bstack1ll11llll11_opy_: str = None
    bstack1ll11l1lll1_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1l1l1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡺࡻࡩࡥࠤᓜ")
    bstack1ll11ll111l_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡯ࡤࠣᓝ")
    bstack1ll11l11l11_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡮ࡢ࡯ࡨࠦᓞ")
    bstack1ll11llll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧ࡫࡯ࡩࡤࡶࡡࡵࡪࠥᓟ")
    bstack1ll1111ll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡶࡤ࡫ࡸࠨᓠ")
    bstack1lll1lll1ll_opy_ = bstack1ll1ll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡸࡻ࡬ࡵࠤᓡ")
    bstack1ll111ll1ll_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡹࡵ࡭ࡶࡢࡥࡹࠨᓢ")
    bstack1ll1l1l1111_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᓣ")
    bstack1ll11ll1lll_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᓤ")
    bstack1ll11lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠣᓥ")
    bstack1llll11111l_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠣᓦ")
    bstack1llll111111_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧᓧ")
    bstack1ll11l1l1ll_opy_ = bstack1ll1ll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡦࡳࡩ࡫ࠢᓨ")
    bstack1ll11lll11l_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠢᓩ")
    bstack1111111ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࠢᓪ")
    bstack1lll1ll1111_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡡࡪ࡮ࡸࡶࡪࠨᓫ")
    bstack1ll11llllll_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠧᓬ")
    bstack1ll1l1111l1_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡭ࡱࡪࡷࠧᓭ")
    bstack1ll1ll11111_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡸࡪࡹࡴࡠ࡯ࡨࡸࡦࠨᓮ")
    bstack1l1111l1l1l_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡶࡧࡴࡶࡥࡴࠩᓯ")
    bstack1lll11l1lll_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨᓰ")
    bstack1ll11111111_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᓱ")
    bstack1ll111lll11_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡥ࡯ࡦࡨࡨࡤࡧࡴࠣᓲ")
    bstack1ll1l1ll11l_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡪࡲࡳࡰࡥࡩࡥࠤᓳ")
    bstack1ll1l11llll_opy_ = bstack1ll1ll1_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡳࡧࡶࡹࡱࡺࠢᓴ")
    bstack1ll1l111111_opy_ = bstack1ll1ll1_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠ࡮ࡲ࡫ࡸࠨᓵ")
    bstack1ll11111ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠢᓶ")
    bstack1ll1l1l1l11_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᓷ")
    bstack1ll1l11111l_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡥ࡭ࡦࡶࡤࡨࡦࡺࡡࠣᓸ")
    bstack1ll11ll1111_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡱࡧࡱࡨ࡮ࡴࡧࠣᓹ")
    bstack1ll11lll111_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤᓺ")
    bstack1l11l1l1111_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࠦᓻ")
    bstack1ll11l1ll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡎࡒࡋࠧᓼ")
    bstack1l11l1lll1l_opy_ = bstack1ll1ll1_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᓽ")
    bstack1lll1l1ll1l_opy_: Dict[str, bstack1llll1l1111_opy_] = dict()
    bstack1l1111l1l11_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll11111l1l_opy_: List[str]
    bstack1ll111l1l11_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll11111l1l_opy_: List[str],
        bstack1ll111l1l11_opy_: Dict[str, str],
        bstack1lll1l11111_opy_: bstack1lll11lllll_opy_
    ):
        self.bstack1ll11111l1l_opy_ = bstack1ll11111l1l_opy_
        self.bstack1ll111l1l11_opy_ = bstack1ll111l1l11_opy_
        self.bstack1lll1l11111_opy_ = bstack1lll1l11111_opy_
    def track_event(
        self,
        context: bstack1ll1l1ll1ll_opy_,
        test_framework_state: bstack1lll1l11lll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࢃࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠥࡧࡲࡨࡵࡀࡿࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻࡾࠤᓾ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll1l1111ll_opy_(
        self,
        instance: bstack1llll1l1111_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1lll111ll_opy_ = TestFramework.bstack1l1lll1lll1_opy_(bstack1llll1l1lll_opy_)
        if not bstack1l1lll111ll_opy_ in TestFramework.bstack1l1111l1l11_opy_:
            return
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡽࢀࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡹࠢᓿ").format(len(TestFramework.bstack1l1111l1l11_opy_[bstack1l1lll111ll_opy_])))
        for callback in TestFramework.bstack1l1111l1l11_opy_[bstack1l1lll111ll_opy_]:
            try:
                callback(self, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack1ll1ll1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠢᔀ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll1l1l11ll_opy_(self):
        return
    @abc.abstractmethod
    def bstack1l1lllll11l_opy_(self, instance, bstack1llll1l1lll_opy_):
        return
    @abc.abstractmethod
    def bstack1ll11ll1ll1_opy_(self, instance, bstack1llll1l1lll_opy_):
        return
    @staticmethod
    def bstack1ll111ll11l_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1lll1111_opy_.create_context(target)
        instance = TestFramework.bstack1lll1l1ll1l_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1llll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l111l11_opy_(reverse=True) -> List[bstack1llll1l1111_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll1l1ll1l_opy_.values(),
            ),
            key=lambda t: t.bstack1lll11111ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11ll11111_opy_(ctx: bstack1lll1l11l11_opy_, reverse=True) -> List[bstack1llll1l1111_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll1l1ll1l_opy_.values(),
            ),
            key=lambda t: t.bstack1lll11111ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllll1ll11_opy_(instance: bstack1llll1l1111_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llll1l1111_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll1l1ll_opy_(instance: bstack1llll1l1111_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡵࡨࡸࡤࡹࡴࡢࡶࡨ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣ࡯ࡪࡿ࠽ࡼࡿࠣࡺࡦࡲࡵࡦ࠿ࡾࢁࠧᔁ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll1ll111l1_opy_(instance: bstack1llll1l1111_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩࡤ࡫࡮ࡵࡴ࡬ࡩࡸࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾࢁࠥ࡫࡮ࡵࡴ࡬ࡩࡸࡃࡻࡾࠤᔂ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l1111l1ll1_opy_(instance: bstack1lll1l11lll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡽࠡ࡭ࡨࡽࡂࢁࡽࠡࡸࡤࡰࡺ࡫࠽ࡼࡿࠥᔃ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll111ll11l_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll111ll11l_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11lll1ll_opy_(instance: bstack1llll1l1111_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll11l1111l_opy_(instance: bstack1llll1l1111_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1lll1lll1_opy_(bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_]):
        return bstack1ll1ll1_opy_ (u"ࠦ࠿ࠨᔄ").join((bstack1lll1l11lll_opy_(bstack1llll1l1lll_opy_[0]).name, bstack1llll1l11l1_opy_(bstack1llll1l1lll_opy_[1]).name))
    @staticmethod
    def bstack1llllll1l1l_opy_(bstack1llll1l1lll_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1llll1l11l1_opy_], callback: Callable):
        bstack1l1lll111ll_opy_ = TestFramework.bstack1l1lll1lll1_opy_(bstack1llll1l1lll_opy_)
        TestFramework.logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡹࡥࡵࡡ࡫ࡳࡴࡱ࡟ࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣ࡬ࡴࡵ࡫ࡠࡴࡨ࡫࡮ࡹࡴࡳࡻࡢ࡯ࡪࡿ࠽ࡼࡿࠥᔅ").format(bstack1l1lll111ll_opy_))
        if not bstack1l1lll111ll_opy_ in TestFramework.bstack1l1111l1l11_opy_:
            TestFramework.bstack1l1111l1l11_opy_[bstack1l1lll111ll_opy_] = []
        TestFramework.bstack1l1111l1l11_opy_[bstack1l1lll111ll_opy_].append(callback)
    @staticmethod
    def bstack1ll1l11lll1_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack1ll1ll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡸ࡮ࡴࡳࠣᔆ"):
            return klass.__qualname__
        return module + bstack1ll1ll1_opy_ (u"ࠢ࠯ࠤᔇ") + klass.__qualname__
    @staticmethod
    def bstack1ll1l1l11l1_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}