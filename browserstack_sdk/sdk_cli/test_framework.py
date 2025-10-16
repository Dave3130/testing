# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
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
from browserstack_sdk.sdk_cli.bstack1lll111111l_opy_ import bstack1ll1lll11l1_opy_, bstack1llll11l111_opy_
class bstack1lll1ll111l_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1ll11_opy_ (u"ࠤࡗࡩࡸࡺࡈࡰࡱ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᓘ").format(self.name)
class bstack1llll111l1l_opy_(Enum):
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
        return bstack1ll11_opy_ (u"ࠥࡘࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡺࡥ࠯ࡽࢀࠦᓙ").format(self.name)
class bstack1llll1111ll_opy_(bstack1ll1lll11l1_opy_):
    bstack1ll11l11lll_opy_: List[str]
    bstack1ll11ll1l11_opy_: Dict[str, str]
    state: bstack1llll111l1l_opy_
    bstack1lll111l1l1_opy_: datetime
    bstack1l1111l11ll_opy_: datetime
    def __init__(
        self,
        context: bstack1llll11l111_opy_,
        bstack1ll11l11lll_opy_: List[str],
        bstack1ll11ll1l11_opy_: Dict[str, str],
        state=bstack1llll111l1l_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll11l11lll_opy_ = bstack1ll11l11lll_opy_
        self.bstack1ll11ll1l11_opy_ = bstack1ll11ll1l11_opy_
        self.state = state
        self.bstack1lll111l1l1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll1ll1ll_opy_(self, bstack1l1111l1l1l_opy_: bstack1llll111l1l_opy_):
        bstack1l1111l1ll1_opy_ = bstack1llll111l1l_opy_(bstack1l1111l1l1l_opy_).name
        if not bstack1l1111l1ll1_opy_:
            return False
        if bstack1l1111l1l1l_opy_ == self.state:
            return False
        self.state = bstack1l1111l1l1l_opy_
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll111ll1ll_opy_:
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
    bstack1ll1l1l1l1l_opy_: int = None
    bstack1l1lllllll1_opy_: str = None
    bstack1lll111_opy_: str = None
    bstack11lll1lll1_opy_: str = None
    bstack1ll11llllll_opy_: str = None
    bstack1ll111l11l1_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1l11ll1_opy_ = bstack1ll11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠢᓚ")
    bstack1ll11ll111l_opy_ = bstack1ll11_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡭ࡩࠨᓛ")
    bstack1ll1ll11111_opy_ = bstack1ll11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠤᓜ")
    bstack1ll1l11l111_opy_ = bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡢࡴࡦࡺࡨࠣᓝ")
    bstack1ll1ll11l1l_opy_ = bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡴࡢࡩࡶࠦᓞ")
    bstack1lll1llll1l_opy_ = bstack1ll11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡶࡹࡱࡺࠢᓟ")
    bstack1l1lllll111_opy_ = bstack1ll11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡷࡺࡲࡴࡠࡣࡷࠦᓠ")
    bstack1ll11lll111_opy_ = bstack1ll11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᓡ")
    bstack1ll1l1l1ll1_opy_ = bstack1ll11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡩࡳࡪࡥࡥࡡࡤࡸࠧᓢ")
    bstack1ll11l1l1l1_opy_ = bstack1ll11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡱࡵࡣࡢࡶ࡬ࡳࡳࠨᓣ")
    bstack1llll111l11_opy_ = bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࠨᓤ")
    bstack1llll1l1l11_opy_ = bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠥᓥ")
    bstack1ll111l1ll1_opy_ = bstack1ll11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡤࡱࡧࡩࠧᓦ")
    bstack1ll1l11l11l_opy_ = bstack1ll11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠧᓧ")
    bstack1lllll111ll_opy_ = bstack1ll11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࠧᓨ")
    bstack1llll11l11l_opy_ = bstack1ll11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪࡦ࡯࡬ࡶࡴࡨࠦᓩ")
    bstack1ll1l1l1111_opy_ = bstack1ll11_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠥᓪ")
    bstack1ll11l1111l_opy_ = bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࡤࡲ࡯ࡨࡵࠥᓫ")
    bstack1ll1ll11l11_opy_ = bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡭ࡦࡶࡤࠦᓬ")
    bstack1l1111l1lll_opy_ = bstack1ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡴࡥࡲࡴࡪࡹࠧᓭ")
    bstack1lll11ll1ll_opy_ = bstack1ll11_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᓮ")
    bstack1ll1l1lll11_opy_ = bstack1ll11_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᓯ")
    bstack1ll1l111111_opy_ = bstack1ll11_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡪࡴࡤࡦࡦࡢࡥࡹࠨᓰ")
    bstack1ll1111l11l_opy_ = bstack1ll11_opy_ (u"ࠨࡨࡰࡱ࡮ࡣ࡮ࡪࠢᓱ")
    bstack1ll1l11l1ll_opy_ = bstack1ll11_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡸࡥࡴࡷ࡯ࡸࠧᓲ")
    bstack1ll11l111ll_opy_ = bstack1ll11_opy_ (u"ࠣࡪࡲࡳࡰࡥ࡬ࡰࡩࡶࠦᓳ")
    bstack1ll11ll1111_opy_ = bstack1ll11_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠧᓴ")
    bstack1ll11111111_opy_ = bstack1ll11_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᓵ")
    bstack1ll1l1l11ll_opy_ = bstack1ll11_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࠨᓶ")
    bstack1ll1ll111ll_opy_ = bstack1ll11_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨᓷ")
    bstack1ll1l1l1lll_opy_ = bstack1ll11_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢᓸ")
    bstack1l11ll1l111_opy_ = bstack1ll11_opy_ (u"ࠢࡕࡇࡖࡘࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࠤᓹ")
    bstack1ll1l11ll1l_opy_ = bstack1ll11_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡌࡐࡉࠥᓺ")
    bstack1l11l1l11l1_opy_ = bstack1ll11_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᓻ")
    bstack1llll1111l1_opy_: Dict[str, bstack1llll1111ll_opy_] = dict()
    bstack1l1111l11l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll11l11lll_opy_: List[str]
    bstack1ll11ll1l11_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll11l11lll_opy_: List[str],
        bstack1ll11ll1l11_opy_: Dict[str, str],
        bstack1lll1l11111_opy_: bstack1lll11lllll_opy_
    ):
        self.bstack1ll11l11lll_opy_ = bstack1ll11l11lll_opy_
        self.bstack1ll11ll1l11_opy_ = bstack1ll11ll1l11_opy_
        self.bstack1lll1l11111_opy_ = bstack1lll1l11111_opy_
    def track_event(
        self,
        context: bstack1ll111ll1ll_opy_,
        test_framework_state: bstack1llll111l1l_opy_,
        test_hook_state: bstack1lll1ll111l_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack1ll11_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡿࠣࡥࡷ࡭ࡳ࠾ࡽࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࢃࠢᓼ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1l1llllll11_opy_(
        self,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1lll1l111_opy_ = TestFramework.bstack1l1lll1ll11_opy_(bstack1llll1l1ll1_opy_)
        if not bstack1l1lll1l111_opy_ in TestFramework.bstack1l1111l11l1_opy_:
            return
        self.logger.debug(bstack1ll11_opy_ (u"ࠦ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡻࡾࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࡷࠧᓽ").format(len(TestFramework.bstack1l1111l11l1_opy_[bstack1l1lll1l111_opy_])))
        for callback in TestFramework.bstack1l1111l11l1_opy_[bstack1l1lll1l111_opy_]:
            try:
                callback(self, instance, bstack1llll1l1ll1_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack1ll11_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠧᓾ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll11ll1ll1_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll1ll111l1_opy_(self, instance, bstack1llll1l1ll1_opy_):
        return
    @abc.abstractmethod
    def bstack1ll111l1111_opy_(self, instance, bstack1llll1l1ll1_opy_):
        return
    @staticmethod
    def bstack1ll1l1lllll_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1lll11l1_opy_.create_context(target)
        instance = TestFramework.bstack1llll1111l1_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1llll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l111ll1_opy_(reverse=True) -> List[bstack1llll1111ll_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1llll1111l1_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111l1l1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11ll111ll_opy_(ctx: bstack1llll11l111_opy_, reverse=True) -> List[bstack1llll1111ll_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1llll1111l1_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111l1l1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1111111lll_opy_(instance: bstack1llll1111ll_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llll1111ll_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll1ll1ll_opy_(instance: bstack1llll1111ll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1ll11_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡽࠡ࡭ࡨࡽࡂࢁࡽࠡࡸࡤࡰࡺ࡫࠽ࡼࡿࠥᓿ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11l1l11l_opy_(instance: bstack1llll1111ll_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack1ll11_opy_ (u"ࠢࡴࡧࡷࡣࡸࡺࡡࡵࡧࡢࡩࡳࡺࡲࡪࡧࡶ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣࡩࡳࡺࡲࡪࡧࡶࡁࢀࢃࠢᔀ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l1111l1l11_opy_(instance: bstack1llll111l1l_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1ll11_opy_ (u"ࠣࡷࡳࡨࡦࡺࡥࡠࡵࡷࡥࡹ࡫࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿࢂࠦ࡫ࡦࡻࡀࡿࢂࠦࡶࡢ࡮ࡸࡩࡂࢁࡽࠣᔁ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll1l1lllll_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll1l1lllll_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11lllll1_opy_(instance: bstack1llll1111ll_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll1l11llll_opy_(instance: bstack1llll1111ll_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1lll1ll11_opy_(bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_]):
        return bstack1ll11_opy_ (u"ࠤ࠽ࠦᔂ").join((bstack1llll111l1l_opy_(bstack1llll1l1ll1_opy_[0]).name, bstack1lll1ll111l_opy_(bstack1llll1l1ll1_opy_[1]).name))
    @staticmethod
    def bstack11111111l1_opy_(bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_], callback: Callable):
        bstack1l1lll1l111_opy_ = TestFramework.bstack1l1lll1ll11_opy_(bstack1llll1l1ll1_opy_)
        TestFramework.logger.debug(bstack1ll11_opy_ (u"ࠥࡷࡪࡺ࡟ࡩࡱࡲ࡯ࡤࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡪࡲࡳࡰࡥࡲࡦࡩ࡬ࡷࡹࡸࡹࡠ࡭ࡨࡽࡂࢁࡽࠣᔃ").format(bstack1l1lll1l111_opy_))
        if not bstack1l1lll1l111_opy_ in TestFramework.bstack1l1111l11l1_opy_:
            TestFramework.bstack1l1111l11l1_opy_[bstack1l1lll1l111_opy_] = []
        TestFramework.bstack1l1111l11l1_opy_[bstack1l1lll1l111_opy_].append(callback)
    @staticmethod
    def bstack1ll1111ll1l_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡶ࡬ࡲࡸࠨᔄ"):
            return klass.__qualname__
        return module + bstack1ll11_opy_ (u"ࠧ࠴ࠢᔅ") + klass.__qualname__
    @staticmethod
    def bstack1ll11lll1l1_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}