# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
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
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll1l1111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1ll1lll11l1_opy_, bstack1llll11l1l1_opy_
class bstack1llll1l11l1_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1lllll1_opy_ (u"ࠥࡘࡪࡹࡴࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᓙ").format(self.name)
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
        return bstack1lllll1_opy_ (u"࡙ࠦ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᓚ").format(self.name)
class bstack1lll1l11l11_opy_(bstack1ll1lll11l1_opy_):
    bstack1ll11l1l1l1_opy_: List[str]
    bstack1l1llllllll_opy_: Dict[str, str]
    state: bstack1llll11l1ll_opy_
    bstack1lll111l111_opy_: datetime
    bstack1l1111l1lll_opy_: datetime
    def __init__(
        self,
        context: bstack1llll11l1l1_opy_,
        bstack1ll11l1l1l1_opy_: List[str],
        bstack1l1llllllll_opy_: Dict[str, str],
        state=bstack1llll11l1ll_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll11l1l1l1_opy_ = bstack1ll11l1l1l1_opy_
        self.bstack1l1llllllll_opy_ = bstack1l1llllllll_opy_
        self.state = state
        self.bstack1lll111l111_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l1lll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll1l11l_opy_(self, bstack1l1111l1l1l_opy_: bstack1llll11l1ll_opy_):
        bstack1l1111l11l1_opy_ = bstack1llll11l1ll_opy_(bstack1l1111l1l1l_opy_).name
        if not bstack1l1111l11l1_opy_:
            return False
        if bstack1l1111l1l1l_opy_ == self.state:
            return False
        self.state = bstack1l1111l1l1l_opy_
        self.bstack1l1111l1lll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll1l1ll111_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll1l1l1ll1_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll1l1ll11l_opy_: int = None
    bstack1ll1l11l1ll_opy_: str = None
    bstack11l1l11_opy_: str = None
    bstack11ll1l1lll_opy_: str = None
    bstack1ll1111l111_opy_: str = None
    bstack1ll11l1l11l_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1lllll1_opy_ = bstack1lllll1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠣᓛ")
    bstack1ll1l1l1lll_opy_ = bstack1lllll1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡮ࡪࠢᓜ")
    bstack1ll11l111ll_opy_ = bstack1lllll1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠥᓝ")
    bstack1ll111111ll_opy_ = bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡣࡵࡧࡴࡩࠤᓞ")
    bstack1ll11l11l1l_opy_ = bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡵࡣࡪࡷࠧᓟ")
    bstack1lll1ll1111_opy_ = bstack1lllll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡷࡺࡲࡴࠣᓠ")
    bstack1ll111lllll_opy_ = bstack1lllll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡸࡻ࡬ࡵࡡࡤࡸࠧᓡ")
    bstack1ll1ll11l11_opy_ = bstack1lllll1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᓢ")
    bstack1ll1111l11l_opy_ = bstack1lllll1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡪࡴࡤࡦࡦࡢࡥࡹࠨᓣ")
    bstack1ll11l1ll11_opy_ = bstack1lllll1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢᓤ")
    bstack1lll1ll1l1l_opy_ = bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠢᓥ")
    bstack1lll1llllll_opy_ = bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠦᓦ")
    bstack1ll1l111l11_opy_ = bstack1lllll1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡥࡲࡨࡪࠨᓧ")
    bstack1ll11ll1lll_opy_ = bstack1lllll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪࠨᓨ")
    bstack1111111ll1_opy_ = bstack1lllll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࠨᓩ")
    bstack1lll1l1llll_opy_ = bstack1lllll1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡧࡩ࡭ࡷࡵࡩࠧᓪ")
    bstack1ll11llll1l_opy_ = bstack1lllll1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠦᓫ")
    bstack1ll11l1l1ll_opy_ = bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡬ࡰࡩࡶࠦᓬ")
    bstack1ll1l111ll1_opy_ = bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡮ࡧࡷࡥࠧᓭ")
    bstack1l1111l1ll1_opy_ = bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡵࡦࡳࡵ࡫ࡳࠨᓮ")
    bstack1lll11l1l11_opy_ = bstack1lllll1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟࡯ࡣࡰࡩࠧᓯ")
    bstack1ll1l1ll1l1_opy_ = bstack1lllll1_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᓰ")
    bstack1ll111llll1_opy_ = bstack1lllll1_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᓱ")
    bstack1ll11l11111_opy_ = bstack1lllll1_opy_ (u"ࠢࡩࡱࡲ࡯ࡤ࡯ࡤࠣᓲ")
    bstack1ll111l1lll_opy_ = bstack1lllll1_opy_ (u"ࠣࡪࡲࡳࡰࡥࡲࡦࡵࡸࡰࡹࠨᓳ")
    bstack1ll111ll1l1_opy_ = bstack1lllll1_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟࡭ࡱࡪࡷࠧᓴ")
    bstack1ll1l111lll_opy_ = bstack1lllll1_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪࠨᓵ")
    bstack1ll1l11l1l1_opy_ = bstack1lllll1_opy_ (u"ࠦࡱࡵࡧࡴࠤᓶ")
    bstack1ll1111llll_opy_ = bstack1lllll1_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡤࡳࡥࡵࡣࡧࡥࡹࡧࠢᓷ")
    bstack1ll111l11ll_opy_ = bstack1lllll1_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢᓸ")
    bstack1l1llll1lll_opy_ = bstack1lllll1_opy_ (u"ࠢࡱࡧࡱࡨ࡮ࡴࡧࠣᓹ")
    bstack1l11l1lllll_opy_ = bstack1lllll1_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࠥᓺ")
    bstack1ll11111111_opy_ = bstack1lllll1_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡍࡑࡊࠦᓻ")
    bstack1l11l11llll_opy_ = bstack1lllll1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᓼ")
    bstack1lll1llll11_opy_: Dict[str, bstack1lll1l11l11_opy_] = dict()
    bstack1l1111l11ll_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll11l1l1l1_opy_: List[str]
    bstack1l1llllllll_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll11l1l1l1_opy_: List[str],
        bstack1l1llllllll_opy_: Dict[str, str],
        bstack1lll11lllll_opy_: bstack1lll1l1111l_opy_
    ):
        self.bstack1ll11l1l1l1_opy_ = bstack1ll11l1l1l1_opy_
        self.bstack1l1llllllll_opy_ = bstack1l1llllllll_opy_
        self.bstack1lll11lllll_opy_ = bstack1lll11lllll_opy_
    def track_event(
        self,
        context: bstack1ll1l1ll111_opy_,
        test_framework_state: bstack1llll11l1ll_opy_,
        test_hook_state: bstack1llll1l11l1_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠤࡦࡸࡧࡴ࠿ࡾࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁࡽࠣᓽ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll11lll1ll_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1llll1111_opy_ = TestFramework.bstack1l1lll1lll1_opy_(bstack1lllll111ll_opy_)
        if not bstack1l1llll1111_opy_ in TestFramework.bstack1l1111l11ll_opy_:
            return
        self.logger.debug(bstack1lllll1_opy_ (u"ࠧ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡼࡿࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࡸࠨᓾ").format(len(TestFramework.bstack1l1111l11ll_opy_[bstack1l1llll1111_opy_])))
        for callback in TestFramework.bstack1l1111l11ll_opy_[bstack1l1llll1111_opy_]:
            try:
                callback(self, instance, bstack1lllll111ll_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack1lllll1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࡿࢂࠨᓿ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll11ll1ll1_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll1l111111_opy_(self, instance, bstack1lllll111ll_opy_):
        return
    @abc.abstractmethod
    def bstack1ll11lllll1_opy_(self, instance, bstack1lllll111ll_opy_):
        return
    @staticmethod
    def bstack1ll11lll11l_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1lll11l1_opy_.create_context(target)
        instance = TestFramework.bstack1lll1llll11_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1lll111l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11ll11l1l_opy_(reverse=True) -> List[bstack1lll1l11l11_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll1llll11_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111l111_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11l11ll1l_opy_(ctx: bstack1llll11l1l1_opy_, reverse=True) -> List[bstack1lll1l11l11_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll1llll11_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111l111_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llll1ll1l1_opy_(instance: bstack1lll1l11l11_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1l11l11_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll1l11l_opy_(instance: bstack1lll1l11l11_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1lllll1_opy_ (u"ࠢࡴࡧࡷࡣࡸࡺࡡࡵࡧ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢ࡮ࡩࡾࡃࡻࡾࠢࡹࡥࡱࡻࡥ࠾ࡽࢀࠦᔀ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11ll1111_opy_(instance: bstack1lll1l11l11_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack1lllll1_opy_ (u"ࠣࡵࡨࡸࡤࡹࡴࡢࡶࡨࡣࡪࡴࡴࡳ࡫ࡨࡷ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽࢀࠤࡪࡴࡴࡳ࡫ࡨࡷࡂࢁࡽࠣᔁ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l1111l1l11_opy_(instance: bstack1llll11l1ll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1lllll1_opy_ (u"ࠤࡸࡴࡩࡧࡴࡦࡡࡶࡸࡦࡺࡥ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡬ࡧࡼࡁࢀࢃࠠࡷࡣ࡯ࡹࡪࡃࡻࡾࠤᔂ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll11lll11l_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll11lll11l_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11l1lll1_opy_(instance: bstack1lll1l11l11_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll111l1111_opy_(instance: bstack1lll1l11l11_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1lll1lll1_opy_(bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_]):
        return bstack1lllll1_opy_ (u"ࠥ࠾ࠧᔃ").join((bstack1llll11l1ll_opy_(bstack1lllll111ll_opy_[0]).name, bstack1llll1l11l1_opy_(bstack1lllll111ll_opy_[1]).name))
    @staticmethod
    def bstack11111111ll_opy_(bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_], callback: Callable):
        bstack1l1llll1111_opy_ = TestFramework.bstack1l1lll1lll1_opy_(bstack1lllll111ll_opy_)
        TestFramework.logger.debug(bstack1lllll1_opy_ (u"ࠦࡸ࡫ࡴࡠࡪࡲࡳࡰࡥࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢ࡫ࡳࡴࡱ࡟ࡳࡧࡪ࡭ࡸࡺࡲࡺࡡ࡮ࡩࡾࡃࡻࡾࠤᔄ").format(bstack1l1llll1111_opy_))
        if not bstack1l1llll1111_opy_ in TestFramework.bstack1l1111l11ll_opy_:
            TestFramework.bstack1l1111l11ll_opy_[bstack1l1llll1111_opy_] = []
        TestFramework.bstack1l1111l11ll_opy_[bstack1l1llll1111_opy_].append(callback)
    @staticmethod
    def bstack1ll1l1ll1ll_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡷ࡭ࡳࡹࠢᔅ"):
            return klass.__qualname__
        return module + bstack1lllll1_opy_ (u"ࠨ࠮ࠣᔆ") + klass.__qualname__
    @staticmethod
    def bstack1ll1l11l111_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}