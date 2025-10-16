# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll1l1111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1ll1ll1llll_opy_, bstack1llll11l111_opy_
class bstack1lll1llll1l_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l_opy_ (u"࡚ࠧࡥࡴࡶࡋࡳࡴࡱࡓࡵࡣࡷࡩ࠳ࢁࡽࠣᓛ").format(self.name)
class bstack1lll1l1ll1l_opy_(Enum):
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
        return bstack1l_opy_ (u"ࠨࡔࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᓜ").format(self.name)
class bstack1llll1l1l11_opy_(bstack1ll1ll1llll_opy_):
    bstack1ll11l1llll_opy_: List[str]
    bstack1ll11ll11l1_opy_: Dict[str, str]
    state: bstack1lll1l1ll1l_opy_
    bstack1lll11111ll_opy_: datetime
    bstack1l1111l1lll_opy_: datetime
    def __init__(
        self,
        context: bstack1llll11l111_opy_,
        bstack1ll11l1llll_opy_: List[str],
        bstack1ll11ll11l1_opy_: Dict[str, str],
        state=bstack1lll1l1ll1l_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll11l1llll_opy_ = bstack1ll11l1llll_opy_
        self.bstack1ll11ll11l1_opy_ = bstack1ll11ll11l1_opy_
        self.state = state
        self.bstack1lll11111ll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l1lll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll11ll1_opy_(self, bstack1l1111l1ll1_opy_: bstack1lll1l1ll1l_opy_):
        bstack1l1111l1l11_opy_ = bstack1lll1l1ll1l_opy_(bstack1l1111l1ll1_opy_).name
        if not bstack1l1111l1l11_opy_:
            return False
        if bstack1l1111l1ll1_opy_ == self.state:
            return False
        self.state = bstack1l1111l1ll1_opy_
        self.bstack1l1111l1lll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll11l111ll_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll111l1l1l_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1ll111ll1l1_opy_: int = None
    bstack1ll1l11l111_opy_: str = None
    bstack1ll11l1_opy_: str = None
    bstack11l1l1l11_opy_: str = None
    bstack1ll11ll1l11_opy_: str = None
    bstack1l1lllll11l_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llll11ll11_opy_ = bstack1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡻࡵࡪࡦࠥᓝ")
    bstack1ll1l1111ll_opy_ = bstack1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡩࡥࠤᓞ")
    bstack1ll1l11lll1_opy_ = bstack1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡯ࡣࡰࡩࠧᓟ")
    bstack1ll11l11111_opy_ = bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡥࡰࡢࡶ࡫ࠦᓠ")
    bstack1ll11lll1ll_opy_ = bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡷࡥ࡬ࡹࠢᓡ")
    bstack1lll1ll1lll_opy_ = bstack1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡪࡹࡵ࡭ࡶࠥᓢ")
    bstack1ll1l1l111l_opy_ = bstack1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷ࡫ࡳࡶ࡮ࡷࡣࡦࡺࠢᓣ")
    bstack1ll11l1l1l1_opy_ = bstack1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᓤ")
    bstack1ll1ll11111_opy_ = bstack1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡥ࡯ࡦࡨࡨࡤࡧࡴࠣᓥ")
    bstack1ll111l1ll1_opy_ = bstack1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡭ࡱࡦࡥࡹ࡯࡯࡯ࠤᓦ")
    bstack1llll11111l_opy_ = bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠤᓧ")
    bstack1llll1111l1_opy_ = bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳࠨᓨ")
    bstack1ll1ll11l11_opy_ = bstack1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡧࡴࡪࡥࠣᓩ")
    bstack1ll1111l1ll_opy_ = bstack1l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠣᓪ")
    bstack1llll1lllll_opy_ = bstack1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࠣᓫ")
    bstack1lll1lll1l1_opy_ = bstack1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡢ࡫࡯ࡹࡷ࡫ࠢᓬ")
    bstack1ll1l1ll111_opy_ = bstack1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪࠨᓭ")
    bstack1ll1l11111l_opy_ = bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡠ࡮ࡲ࡫ࡸࠨᓮ")
    bstack1ll111l11ll_opy_ = bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡰࡩࡹࡧࠢᓯ")
    bstack1l1111l11ll_opy_ = bstack1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡷࡨࡵࡰࡦࡵࠪᓰ")
    bstack1lll11lll1l_opy_ = bstack1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡱࡥࡲ࡫ࠢᓱ")
    bstack1ll1l111lll_opy_ = bstack1l_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᓲ")
    bstack1ll111111ll_opy_ = bstack1l_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡦࡰࡧࡩࡩࡥࡡࡵࠤᓳ")
    bstack1ll1l1llll1_opy_ = bstack1l_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟ࡪࡦࠥᓴ")
    bstack1ll1l11l1l1_opy_ = bstack1l_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡴࡨࡷࡺࡲࡴࠣᓵ")
    bstack1ll1l1lll1l_opy_ = bstack1l_opy_ (u"ࠦ࡭ࡵ࡯࡬ࡡ࡯ࡳ࡬ࡹࠢᓶ")
    bstack1ll11llll11_opy_ = bstack1l_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠣᓷ")
    bstack1ll1l111l11_opy_ = bstack1l_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᓸ")
    bstack1ll11ll1lll_opy_ = bstack1l_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠤᓹ")
    bstack1ll111l1l11_opy_ = bstack1l_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤᓺ")
    bstack1ll111lllll_opy_ = bstack1l_opy_ (u"ࠤࡳࡩࡳࡪࡩ࡯ࡩࠥᓻ")
    bstack1l11ll1l11l_opy_ = bstack1l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠧᓼ")
    bstack1ll11111l11_opy_ = bstack1l_opy_ (u"࡙ࠦࡋࡓࡕࡡࡏࡓࡌࠨᓽ")
    bstack1l11l11111l_opy_ = bstack1l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᓾ")
    bstack1llll11l1ll_opy_: Dict[str, bstack1llll1l1l11_opy_] = dict()
    bstack1l1111l11l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll11l1llll_opy_: List[str]
    bstack1ll11ll11l1_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll11l1llll_opy_: List[str],
        bstack1ll11ll11l1_opy_: Dict[str, str],
        bstack1lll1l11111_opy_: bstack1lll1l1111l_opy_
    ):
        self.bstack1ll11l1llll_opy_ = bstack1ll11l1llll_opy_
        self.bstack1ll11ll11l1_opy_ = bstack1ll11ll11l1_opy_
        self.bstack1lll1l11111_opy_ = bstack1lll1l11111_opy_
    def track_event(
        self,
        context: bstack1ll11l111ll_opy_,
        test_framework_state: bstack1lll1l1ll1l_opy_,
        test_hook_state: bstack1lll1llll1l_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack1l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡽࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠦࡡࡳࡩࡶࡁࢀࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼࡿࠥᓿ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll1111ll1l_opy_(
        self,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1llll1111_opy_ = TestFramework.bstack1l1lll11ll1_opy_(bstack1lllll1ll11_opy_)
        if not bstack1l1llll1111_opy_ in TestFramework.bstack1l1111l11l1_opy_:
            return
        self.logger.debug(bstack1l_opy_ (u"ࠢࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡾࢁࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࡳࠣᔀ").format(len(TestFramework.bstack1l1111l11l1_opy_[bstack1l1llll1111_opy_])))
        for callback in TestFramework.bstack1l1111l11l1_opy_[bstack1l1llll1111_opy_]:
            try:
                callback(self, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack1l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠣᔁ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll111lll11_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll1l111ll1_opy_(self, instance, bstack1lllll1ll11_opy_):
        return
    @abc.abstractmethod
    def bstack1ll111llll1_opy_(self, instance, bstack1lllll1ll11_opy_):
        return
    @staticmethod
    def bstack1ll11ll1ll1_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1ll1llll_opy_.create_context(target)
        instance = TestFramework.bstack1llll11l1ll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1lll111l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11ll1l111_opy_(reverse=True) -> List[bstack1llll1l1l11_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1llll11l1ll_opy_.values(),
            ),
            key=lambda t: t.bstack1lll11111ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11ll111ll_opy_(ctx: bstack1llll11l111_opy_, reverse=True) -> List[bstack1llll1l1l11_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1llll11l1ll_opy_.values(),
            ),
            key=lambda t: t.bstack1lll11111ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llllllll11_opy_(instance: bstack1llll1l1l11_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llll1l1l11_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll11ll1_opy_(instance: bstack1llll1l1l11_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽࢀࠤࡰ࡫ࡹ࠾ࡽࢀࠤࡻࡧ࡬ࡶࡧࡀࡿࢂࠨᔂ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11111111_opy_(instance: bstack1llll1l1l11_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack1l_opy_ (u"ࠥࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡥࡥ࡯ࡶࡵ࡭ࡪࡹ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿࢂࠦࡥ࡯ࡶࡵ࡭ࡪࡹ࠽ࡼࡿࠥᔃ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l1111l1l1l_opy_(instance: bstack1lll1l1ll1l_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l_opy_ (u"ࠦࡺࡶࡤࡢࡶࡨࡣࡸࡺࡡࡵࡧ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢ࡮ࡩࡾࡃࡻࡾࠢࡹࡥࡱࡻࡥ࠾ࡽࢀࠦᔄ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll11ll1ll1_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll11ll1ll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll1111ll11_opy_(instance: bstack1llll1l1l11_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll11llll1l_opy_(instance: bstack1llll1l1l11_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1lll11ll1_opy_(bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_]):
        return bstack1l_opy_ (u"ࠧࡀࠢᔅ").join((bstack1lll1l1ll1l_opy_(bstack1lllll1ll11_opy_[0]).name, bstack1lll1llll1l_opy_(bstack1lllll1ll11_opy_[1]).name))
    @staticmethod
    def bstack1lllll1111l_opy_(bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_], callback: Callable):
        bstack1l1llll1111_opy_ = TestFramework.bstack1l1lll11ll1_opy_(bstack1lllll1ll11_opy_)
        TestFramework.logger.debug(bstack1l_opy_ (u"ࠨࡳࡦࡶࡢ࡬ࡴࡵ࡫ࡠࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤ࡭ࡵ࡯࡬ࡡࡵࡩ࡬࡯ࡳࡵࡴࡼࡣࡰ࡫ࡹ࠾ࡽࢀࠦᔆ").format(bstack1l1llll1111_opy_))
        if not bstack1l1llll1111_opy_ in TestFramework.bstack1l1111l11l1_opy_:
            TestFramework.bstack1l1111l11l1_opy_[bstack1l1llll1111_opy_] = []
        TestFramework.bstack1l1111l11l1_opy_[bstack1l1llll1111_opy_].append(callback)
    @staticmethod
    def bstack1ll1l111111_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡹ࡯࡮ࡴࠤᔇ"):
            return klass.__qualname__
        return module + bstack1l_opy_ (u"ࠣ࠰ࠥᔈ") + klass.__qualname__
    @staticmethod
    def bstack1ll1l1l1ll1_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}