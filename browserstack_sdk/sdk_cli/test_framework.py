# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
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
from browserstack_sdk.sdk_cli.bstack1lll1111l1l_opy_ import bstack1ll1ll1llll_opy_, bstack1lll1ll111l_opy_
class bstack1llll1111l1_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l1l11_opy_ (u"ࠤࡗࡩࡸࡺࡈࡰࡱ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᓑ").format(self.name)
class bstack1lll1lllll1_opy_(Enum):
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
        return bstack11l1l11_opy_ (u"ࠥࡘࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡺࡥ࠯ࡽࢀࠦᓒ").format(self.name)
class bstack1lll1l1ll11_opy_(bstack1ll1ll1llll_opy_):
    bstack1ll11ll1l11_opy_: List[str]
    bstack1ll1l1ll1l1_opy_: Dict[str, str]
    state: bstack1lll1lllll1_opy_
    bstack1lll1111111_opy_: datetime
    bstack1l1111l11l1_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1ll111l_opy_,
        bstack1ll11ll1l11_opy_: List[str],
        bstack1ll1l1ll1l1_opy_: Dict[str, str],
        state=bstack1lll1lllll1_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll11ll1l11_opy_ = bstack1ll11ll1l11_opy_
        self.bstack1ll1l1ll1l1_opy_ = bstack1ll1l1ll1l1_opy_
        self.state = state
        self.bstack1lll1111111_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l11l1_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll1l1l1l_opy_(self, bstack1l1111l1l1l_opy_: bstack1lll1lllll1_opy_):
        bstack1l1111l1l11_opy_ = bstack1lll1lllll1_opy_(bstack1l1111l1l1l_opy_).name
        if not bstack1l1111l1l11_opy_:
            return False
        if bstack1l1111l1l1l_opy_ == self.state:
            return False
        self.state = bstack1l1111l1l1l_opy_
        self.bstack1l1111l11l1_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll1l1lll11_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll111l1ll1_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll111ll11l_opy_: int = None
    bstack1ll1l11ll1l_opy_: str = None
    bstack111l11l_opy_: str = None
    bstack1111l1lll1_opy_: str = None
    bstack1ll11l1l111_opy_: str = None
    bstack1ll1ll111ll_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llll11l1ll_opy_ = bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠢᓓ")
    bstack1ll1l11llll_opy_ = bstack11l1l11_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡭ࡩࠨᓔ")
    bstack1ll11111lll_opy_ = bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠤᓕ")
    bstack1ll11l1lll1_opy_ = bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡢࡴࡦࡺࡨࠣᓖ")
    bstack1ll1l1l111l_opy_ = bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡴࡢࡩࡶࠦᓗ")
    bstack1llll111ll1_opy_ = bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡶࡹࡱࡺࠢᓘ")
    bstack1ll111lll1l_opy_ = bstack11l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡷࡺࡲࡴࡠࡣࡷࠦᓙ")
    bstack1ll1111ll11_opy_ = bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᓚ")
    bstack1ll1l11l11l_opy_ = bstack11l1l11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡩࡳࡪࡥࡥࡡࡤࡸࠧᓛ")
    bstack1ll1ll11111_opy_ = bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣࡱࡵࡣࡢࡶ࡬ࡳࡳࠨᓜ")
    bstack1lll1l11l1l_opy_ = bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࠨᓝ")
    bstack1lll1l1111l_opy_ = bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠥᓞ")
    bstack1ll111llll1_opy_ = bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡤࡱࡧࡩࠧᓟ")
    bstack1ll11llllll_opy_ = bstack11l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠧᓠ")
    bstack1llll1ll111_opy_ = bstack11l1l11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࠧᓡ")
    bstack1lll1ll1ll1_opy_ = bstack11l1l11_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪࡦ࡯࡬ࡶࡴࡨࠦᓢ")
    bstack1ll111ll1ll_opy_ = bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠥᓣ")
    bstack1ll1l11l1ll_opy_ = bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡤࡲ࡯ࡨࡵࠥᓤ")
    bstack1ll111l11l1_opy_ = bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡭ࡦࡶࡤࠦᓥ")
    bstack1l1111l1111_opy_ = bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡴࡥࡲࡴࡪࡹࠧᓦ")
    bstack1lll11l1l1l_opy_ = bstack11l1l11_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᓧ")
    bstack1ll1l1llll1_opy_ = bstack11l1l11_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᓨ")
    bstack1ll11l1l1l1_opy_ = bstack11l1l11_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡪࡴࡤࡦࡦࡢࡥࡹࠨᓩ")
    bstack1ll111ll111_opy_ = bstack11l1l11_opy_ (u"ࠨࡨࡰࡱ࡮ࡣ࡮ࡪࠢᓪ")
    bstack1ll1l1ll111_opy_ = bstack11l1l11_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡸࡥࡴࡷ࡯ࡸࠧᓫ")
    bstack1ll11ll11l1_opy_ = bstack11l1l11_opy_ (u"ࠣࡪࡲࡳࡰࡥ࡬ࡰࡩࡶࠦᓬ")
    bstack1ll111l11ll_opy_ = bstack11l1l11_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠧᓭ")
    bstack1ll1l1l1lll_opy_ = bstack11l1l11_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᓮ")
    bstack1ll111lllll_opy_ = bstack11l1l11_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࠨᓯ")
    bstack1ll11lll1l1_opy_ = bstack11l1l11_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨᓰ")
    bstack1ll11ll1l1l_opy_ = bstack11l1l11_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢᓱ")
    bstack1l11l1ll1l1_opy_ = bstack11l1l11_opy_ (u"ࠢࡕࡇࡖࡘࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࠤᓲ")
    bstack1ll1111l11l_opy_ = bstack11l1l11_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡌࡐࡉࠥᓳ")
    bstack1l11l11l11l_opy_ = bstack11l1l11_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᓴ")
    bstack1lll1lll111_opy_: Dict[str, bstack1lll1l1ll11_opy_] = dict()
    bstack1l1111l11ll_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll11ll1l11_opy_: List[str]
    bstack1ll1l1ll1l1_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll11ll1l11_opy_: List[str],
        bstack1ll1l1ll1l1_opy_: Dict[str, str],
        bstack1lll1l11111_opy_: bstack1lll11lllll_opy_
    ):
        self.bstack1ll11ll1l11_opy_ = bstack1ll11ll1l11_opy_
        self.bstack1ll1l1ll1l1_opy_ = bstack1ll1l1ll1l1_opy_
        self.bstack1lll1l11111_opy_ = bstack1lll1l11111_opy_
    def track_event(
        self,
        context: bstack1ll1l1lll11_opy_,
        test_framework_state: bstack1lll1lllll1_opy_,
        test_hook_state: bstack1llll1111l1_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡿࠣࡥࡷ࡭ࡳ࠾ࡽࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࢃࠢᓵ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll1l1111l1_opy_(
        self,
        instance: bstack1lll1l1ll11_opy_,
        bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1lll1l1l1_opy_ = TestFramework.bstack1l1llll1111_opy_(bstack11111111l1_opy_)
        if not bstack1l1lll1l1l1_opy_ in TestFramework.bstack1l1111l11ll_opy_:
            return
        self.logger.debug(bstack11l1l11_opy_ (u"ࠦ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡻࡾࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࡷࠧᓶ").format(len(TestFramework.bstack1l1111l11ll_opy_[bstack1l1lll1l1l1_opy_])))
        for callback in TestFramework.bstack1l1111l11ll_opy_[bstack1l1lll1l1l1_opy_]:
            try:
                callback(self, instance, bstack11111111l1_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack11l1l11_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠧᓷ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll1l1l11l1_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll111lll11_opy_(self, instance, bstack11111111l1_opy_):
        return
    @abc.abstractmethod
    def bstack1ll11l1llll_opy_(self, instance, bstack11111111l1_opy_):
        return
    @staticmethod
    def bstack1ll11111111_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1ll1llll_opy_.create_context(target)
        instance = TestFramework.bstack1lll1lll111_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1lll1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l11lll1_opy_(reverse=True) -> List[bstack1lll1l1ll11_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll1lll111_opy_.values(),
            ),
            key=lambda t: t.bstack1lll1111111_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11l11ll11_opy_(ctx: bstack1lll1ll111l_opy_, reverse=True) -> List[bstack1lll1l1ll11_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll1lll111_opy_.values(),
            ),
            key=lambda t: t.bstack1lll1111111_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1111111ll1_opy_(instance: bstack1lll1l1ll11_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1l1ll11_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll1l1l1l_opy_(instance: bstack1lll1l1ll11_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l1l11_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡽࠡ࡭ࡨࡽࡂࢁࡽࠡࡸࡤࡰࡺ࡫࠽ࡼࡿࠥᓸ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1l1lllll11l_opy_(instance: bstack1lll1l1ll11_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack11l1l11_opy_ (u"ࠢࡴࡧࡷࡣࡸࡺࡡࡵࡧࡢࡩࡳࡺࡲࡪࡧࡶ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣࡩࡳࡺࡲࡪࡧࡶࡁࢀࢃࠢᓹ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l1111l111l_opy_(instance: bstack1lll1lllll1_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l1l11_opy_ (u"ࠣࡷࡳࡨࡦࡺࡥࡠࡵࡷࡥࡹ࡫࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿࢂࠦ࡫ࡦࡻࡀࡿࢂࠦࡶࡢ࡮ࡸࡩࡂࢁࡽࠣᓺ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll11111111_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll11111111_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll111111l1_opy_(instance: bstack1lll1l1ll11_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll111l111l_opy_(instance: bstack1lll1l1ll11_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1llll1111_opy_(bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_]):
        return bstack11l1l11_opy_ (u"ࠤ࠽ࠦᓻ").join((bstack1lll1lllll1_opy_(bstack11111111l1_opy_[0]).name, bstack1llll1111l1_opy_(bstack11111111l1_opy_[1]).name))
    @staticmethod
    def bstack111111l11l_opy_(bstack11111111l1_opy_: Tuple[bstack1lll1lllll1_opy_, bstack1llll1111l1_opy_], callback: Callable):
        bstack1l1lll1l1l1_opy_ = TestFramework.bstack1l1llll1111_opy_(bstack11111111l1_opy_)
        TestFramework.logger.debug(bstack11l1l11_opy_ (u"ࠥࡷࡪࡺ࡟ࡩࡱࡲ࡯ࡤࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡪࡲࡳࡰࡥࡲࡦࡩ࡬ࡷࡹࡸࡹࡠ࡭ࡨࡽࡂࢁࡽࠣᓼ").format(bstack1l1lll1l1l1_opy_))
        if not bstack1l1lll1l1l1_opy_ in TestFramework.bstack1l1111l11ll_opy_:
            TestFramework.bstack1l1111l11ll_opy_[bstack1l1lll1l1l1_opy_] = []
        TestFramework.bstack1l1111l11ll_opy_[bstack1l1lll1l1l1_opy_].append(callback)
    @staticmethod
    def bstack1ll111l1l1l_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡶ࡬ࡲࡸࠨᓽ"):
            return klass.__qualname__
        return module + bstack11l1l11_opy_ (u"ࠧ࠴ࠢᓾ") + klass.__qualname__
    @staticmethod
    def bstack1ll1l11lll1_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}