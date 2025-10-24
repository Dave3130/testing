# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll11ll111_opy_ import bstack1lll11l1lll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llll111_opy_ import bstack1ll1ll11ll1_opy_, bstack1llll111l1l_opy_
class bstack1lll1ll1111_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l11l1_opy_ (u"ࠥࡘࡪࡹࡴࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᓮ").format(self.name)
class bstack1lll1l1lll1_opy_(Enum):
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
        return bstack11l11l1_opy_ (u"࡙ࠦ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᓯ").format(self.name)
class bstack1lll1l11111_opy_(bstack1ll1ll11ll1_opy_):
    bstack1l1llll1lll_opy_: List[str]
    bstack1ll1l11ll11_opy_: Dict[str, str]
    state: bstack1lll1l1lll1_opy_
    bstack1lll1111111_opy_: datetime
    bstack1l11111l1l1_opy_: datetime
    def __init__(
        self,
        context: bstack1llll111l1l_opy_,
        bstack1l1llll1lll_opy_: List[str],
        bstack1ll1l11ll11_opy_: Dict[str, str],
        state=bstack1lll1l1lll1_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1l1llll1lll_opy_ = bstack1l1llll1lll_opy_
        self.bstack1ll1l11ll11_opy_ = bstack1ll1l11ll11_opy_
        self.state = state
        self.bstack1lll1111111_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l11111l1l1_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llllllllll_opy_(self, bstack1l11111l1ll_opy_: bstack1lll1l1lll1_opy_):
        bstack1l11111ll1l_opy_ = bstack1lll1l1lll1_opy_(bstack1l11111l1ll_opy_).name
        if not bstack1l11111ll1l_opy_:
            return False
        if bstack1l11111l1ll_opy_ == self.state:
            return False
        self.state = bstack1l11111l1ll_opy_
        self.bstack1l11111l1l1_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll1l111l11_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll1111111l_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll111lll11_opy_: int = None
    bstack1ll1l11lll1_opy_: str = None
    bstack1111ll1_opy_: str = None
    bstack11ll11lll1_opy_: str = None
    bstack1ll1l1ll111_opy_: str = None
    bstack1ll1l1ll1l1_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1l11l11_opy_ = bstack11l11l1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠣᓰ")
    bstack1ll1111l1ll_opy_ = bstack11l11l1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡮ࡪࠢᓱ")
    bstack1ll1l1ll1ll_opy_ = bstack11l11l1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠥᓲ")
    bstack1ll111l1111_opy_ = bstack11l11l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡣࡵࡧࡴࡩࠤᓳ")
    bstack1ll1l11l1ll_opy_ = bstack11l11l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡵࡣࡪࡷࠧᓴ")
    bstack1lll11lll11_opy_ = bstack11l11l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡷࡺࡲࡴࠣᓵ")
    bstack1ll1l1l1l1l_opy_ = bstack11l11l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡸࡻ࡬ࡵࡡࡤࡸࠧᓶ")
    bstack1ll1111l11l_opy_ = bstack11l11l1_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᓷ")
    bstack1l1lllll111_opy_ = bstack11l11l1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡪࡴࡤࡦࡦࡢࡥࡹࠨᓸ")
    bstack1ll1111ll1l_opy_ = bstack11l11l1_opy_ (u"ࠢࡵࡧࡶࡸࡤࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢᓹ")
    bstack1lll1ll11ll_opy_ = bstack11l11l1_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠢᓺ")
    bstack1lll1l1ll11_opy_ = bstack11l11l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠦᓻ")
    bstack1ll11l1l1ll_opy_ = bstack11l11l1_opy_ (u"ࠥࡸࡪࡹࡴࡠࡥࡲࡨࡪࠨᓼ")
    bstack1ll11l11111_opy_ = bstack11l11l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪࠨᓽ")
    bstack1lllll11111_opy_ = bstack11l11l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࠨᓾ")
    bstack1lll1l11lll_opy_ = bstack11l11l1_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡧࡩ࡭ࡷࡵࡩࠧᓿ")
    bstack1ll1111lll1_opy_ = bstack11l11l1_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠦᔀ")
    bstack1l1lllll1l1_opy_ = bstack11l11l1_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡬ࡰࡩࡶࠦᔁ")
    bstack1ll11l11lll_opy_ = bstack11l11l1_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡮ࡧࡷࡥࠧᔂ")
    bstack1l11111ll11_opy_ = bstack11l11l1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡵࡦࡳࡵ࡫ࡳࠨᔃ")
    bstack1lll1111l1l_opy_ = bstack11l11l1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟࡯ࡣࡰࡩࠧᔄ")
    bstack1ll111llll1_opy_ = bstack11l11l1_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᔅ")
    bstack1ll1l11llll_opy_ = bstack11l11l1_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᔆ")
    bstack1l1llll11l1_opy_ = bstack11l11l1_opy_ (u"ࠢࡩࡱࡲ࡯ࡤ࡯ࡤࠣᔇ")
    bstack1ll111l11ll_opy_ = bstack11l11l1_opy_ (u"ࠣࡪࡲࡳࡰࡥࡲࡦࡵࡸࡰࡹࠨᔈ")
    bstack1ll111lll1l_opy_ = bstack11l11l1_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟࡭ࡱࡪࡷࠧᔉ")
    bstack1ll111l1ll1_opy_ = bstack11l11l1_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪࠨᔊ")
    bstack1ll111l1l11_opy_ = bstack11l11l1_opy_ (u"ࠦࡱࡵࡧࡴࠤᔋ")
    bstack1ll11ll11l1_opy_ = bstack11l11l1_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡤࡳࡥࡵࡣࡧࡥࡹࡧࠢᔌ")
    bstack1l1llll111l_opy_ = bstack11l11l1_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢᔍ")
    bstack1ll11lllll1_opy_ = bstack11l11l1_opy_ (u"ࠢࡱࡧࡱࡨ࡮ࡴࡧࠣᔎ")
    bstack1l11l1l1111_opy_ = bstack11l11l1_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࠥᔏ")
    bstack1ll11lll1l1_opy_ = bstack11l11l1_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡍࡑࡊࠦᔐ")
    bstack1l11l1lll11_opy_ = bstack11l11l1_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᔑ")
    bstack1lll1l1llll_opy_: Dict[str, bstack1lll1l11111_opy_] = dict()
    bstack1l11111lll1_opy_: Dict[str, List[Callable]] = dict()
    bstack1l1llll1lll_opy_: List[str]
    bstack1ll1l11ll11_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1l1llll1lll_opy_: List[str],
        bstack1ll1l11ll11_opy_: Dict[str, str],
        bstack1lll11ll111_opy_: bstack1lll11l1lll_opy_
    ):
        self.bstack1l1llll1lll_opy_ = bstack1l1llll1lll_opy_
        self.bstack1ll1l11ll11_opy_ = bstack1ll1l11ll11_opy_
        self.bstack1lll11ll111_opy_ = bstack1lll11ll111_opy_
    def track_event(
        self,
        context: bstack1ll1l111l11_opy_,
        test_framework_state: bstack1lll1l1lll1_opy_,
        test_hook_state: bstack1lll1ll1111_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠤࡦࡸࡧࡴ࠿ࡾࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁࡽࠣᔒ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll11l1ll1l_opy_(
        self,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1ll111_opy_ = TestFramework.bstack1l1lll1l11l_opy_(bstack1lllllll1l1_opy_)
        if not bstack1l1ll1ll111_opy_ in TestFramework.bstack1l11111lll1_opy_:
            return
        self.logger.debug(bstack11l11l1_opy_ (u"ࠧ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡼࡿࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࡸࠨᔓ").format(len(TestFramework.bstack1l11111lll1_opy_[bstack1l1ll1ll111_opy_])))
        for callback in TestFramework.bstack1l11111lll1_opy_[bstack1l1ll1ll111_opy_]:
            try:
                callback(self, instance, bstack1lllllll1l1_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack11l11l1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࡿࢂࠨᔔ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll111ll1ll_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll11l1l1l1_opy_(self, instance, bstack1lllllll1l1_opy_):
        return
    @abc.abstractmethod
    def bstack1ll11ll1l11_opy_(self, instance, bstack1lllllll1l1_opy_):
        return
    @staticmethod
    def bstack1ll1111l111_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        instance = TestFramework.bstack1lll1l1llll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1l11l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1l11ll_opy_(reverse=True) -> List[bstack1lll1l11111_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll1l1llll_opy_.values(),
            ),
            key=lambda t: t.bstack1lll1111111_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11l11111l_opy_(ctx: bstack1llll111l1l_opy_, reverse=True) -> List[bstack1lll1l11111_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll1l1llll_opy_.values(),
            ),
            key=lambda t: t.bstack1lll1111111_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllll1l1ll_opy_(instance: bstack1lll1l11111_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1l11111_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llllllllll_opy_(instance: bstack1lll1l11111_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l11l1_opy_ (u"ࠢࡴࡧࡷࡣࡸࡺࡡࡵࡧ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢ࡮ࡩࡾࡃࡻࡾࠢࡹࡥࡱࡻࡥ࠾ࡽࢀࠦᔕ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll111111l1_opy_(instance: bstack1lll1l11111_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack11l11l1_opy_ (u"ࠣࡵࡨࡸࡤࡹࡴࡢࡶࡨࡣࡪࡴࡴࡳ࡫ࡨࡷ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽࢀࠤࡪࡴࡴࡳ࡫ࡨࡷࡂࢁࡽࠣᔖ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l11111l11l_opy_(instance: bstack1lll1l1lll1_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11l11l1_opy_ (u"ࠤࡸࡴࡩࡧࡴࡦࡡࡶࡸࡦࡺࡥ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡬ࡧࡼࡁࢀࢃࠠࡷࡣ࡯ࡹࡪࡃࡻࡾࠤᔗ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll1111l111_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll1111l111_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll1l1l1lll_opy_(instance: bstack1lll1l11111_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1l1llll1l11_opy_(instance: bstack1lll1l11111_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1lll1l11l_opy_(bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_]):
        return bstack11l11l1_opy_ (u"ࠥ࠾ࠧᔘ").join((bstack1lll1l1lll1_opy_(bstack1lllllll1l1_opy_[0]).name, bstack1lll1ll1111_opy_(bstack1lllllll1l1_opy_[1]).name))
    @staticmethod
    def bstack1llll1l1l11_opy_(bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_], callback: Callable):
        bstack1l1ll1ll111_opy_ = TestFramework.bstack1l1lll1l11l_opy_(bstack1lllllll1l1_opy_)
        TestFramework.logger.debug(bstack11l11l1_opy_ (u"ࠦࡸ࡫ࡴࡠࡪࡲࡳࡰࡥࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢ࡫ࡳࡴࡱ࡟ࡳࡧࡪ࡭ࡸࡺࡲࡺࡡ࡮ࡩࡾࡃࡻࡾࠤᔙ").format(bstack1l1ll1ll111_opy_))
        if not bstack1l1ll1ll111_opy_ in TestFramework.bstack1l11111lll1_opy_:
            TestFramework.bstack1l11111lll1_opy_[bstack1l1ll1ll111_opy_] = []
        TestFramework.bstack1l11111lll1_opy_[bstack1l1ll1ll111_opy_].append(callback)
    @staticmethod
    def bstack1ll11111lll_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack11l11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡷ࡭ࡳࡹࠢᔚ"):
            return klass.__qualname__
        return module + bstack11l11l1_opy_ (u"ࠨ࠮ࠣᔛ") + klass.__qualname__
    @staticmethod
    def bstack1l1llllllll_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}