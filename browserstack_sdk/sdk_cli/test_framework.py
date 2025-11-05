# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll11l111l_opy_ import bstack1lll111llll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llll1ll_opy_ import bstack1ll1l1lllll_opy_, bstack1lll1llllll_opy_
class bstack1lll1ll1l1l_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11111_opy_ (u"ࠤࡗࡩࡸࡺࡈࡰࡱ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᔗ").format(self.name)
class bstack1lll1ll111l_opy_(Enum):
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
        return bstack11111_opy_ (u"ࠥࡘࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡺࡥ࠯ࡽࢀࠦᔘ").format(self.name)
class bstack1lll1l1ll1l_opy_(bstack1ll1l1lllll_opy_):
    bstack1ll11llllll_opy_: List[str]
    bstack1ll1l11l111_opy_: Dict[str, str]
    state: bstack1lll1ll111l_opy_
    bstack1ll1lll1ll1_opy_: datetime
    bstack11lllllllll_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1llllll_opy_,
        bstack1ll11llllll_opy_: List[str],
        bstack1ll1l11l111_opy_: Dict[str, str],
        state=bstack1lll1ll111l_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll11llllll_opy_ = bstack1ll11llllll_opy_
        self.bstack1ll1l11l111_opy_ = bstack1ll1l11l111_opy_
        self.state = state
        self.bstack1ll1lll1ll1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack11lllllllll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllllll11l_opy_(self, bstack1l1111111ll_opy_: bstack1lll1ll111l_opy_):
        bstack11llllllll1_opy_ = bstack1lll1ll111l_opy_(bstack1l1111111ll_opy_).name
        if not bstack11llllllll1_opy_:
            return False
        if bstack1l1111111ll_opy_ == self.state:
            return False
        self.state = bstack1l1111111ll_opy_
        self.bstack11lllllllll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll1l11ll1l_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1ll111lll1l_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1l1lllllll1_opy_: int = None
    bstack1l1llll111l_opy_: str = None
    bstack11ll111_opy_: str = None
    bstack11lll1l1ll_opy_: str = None
    bstack1ll11l111l1_opy_: str = None
    bstack1l1llll1l11_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1lll1ll_opy_ = bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠢᔙ")
    bstack1l1lll1l11l_opy_ = bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡭ࡩࠨᔚ")
    bstack1ll1l11l11l_opy_ = bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠤᔛ")
    bstack1l1lll1ll11_opy_ = bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡢࡴࡦࡺࡨࠣᔜ")
    bstack1l1lllll111_opy_ = bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡴࡢࡩࡶࠦᔝ")
    bstack1lll11llll1_opy_ = bstack11111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡶࡹࡱࡺࠢᔞ")
    bstack1ll111l11ll_opy_ = bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡷࡺࡲࡴࡠࡣࡷࠦᔟ")
    bstack1l1lll1l1ll_opy_ = bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᔠ")
    bstack1ll11l11l1l_opy_ = bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡩࡳࡪࡥࡥࡡࡤࡸࠧᔡ")
    bstack1ll111l1l1l_opy_ = bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡱࡵࡣࡢࡶ࡬ࡳࡳࠨᔢ")
    bstack1lll11l11l1_opy_ = bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࠨᔣ")
    bstack1lll11lll1l_opy_ = bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠥᔤ")
    bstack1ll111l11l1_opy_ = bstack11111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡤࡱࡧࡩࠧᔥ")
    bstack1ll111ll1l1_opy_ = bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠧᔦ")
    bstack1lllll1ll11_opy_ = bstack11111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࠧᔧ")
    bstack1lll1l11lll_opy_ = bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪࡦ࡯࡬ࡶࡴࡨࠦᔨ")
    bstack1ll1111llll_opy_ = bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠥᔩ")
    bstack1ll11l1l111_opy_ = bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡤࡲ࡯ࡨࡵࠥᔪ")
    bstack1l1llll11l1_opy_ = bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡭ࡦࡶࡤࠦᔫ")
    bstack1l1111111l1_opy_ = bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡴࡥࡲࡴࡪࡹࠧᔬ")
    bstack1ll1lllll11_opy_ = bstack11111_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᔭ")
    bstack1l1llllll1l_opy_ = bstack11111_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᔮ")
    bstack1ll111ll1ll_opy_ = bstack11111_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡪࡴࡤࡦࡦࡢࡥࡹࠨᔯ")
    bstack1ll1l1l1l1l_opy_ = bstack11111_opy_ (u"ࠨࡨࡰࡱ࡮ࡣ࡮ࡪࠢᔰ")
    bstack1ll11l11111_opy_ = bstack11111_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡸࡥࡴࡷ࡯ࡸࠧᔱ")
    bstack1ll1l11llll_opy_ = bstack11111_opy_ (u"ࠣࡪࡲࡳࡰࡥ࡬ࡰࡩࡶࠦᔲ")
    bstack1l1llll11ll_opy_ = bstack11111_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠧᔳ")
    bstack1ll1l111111_opy_ = bstack11111_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᔴ")
    bstack1ll111l1l11_opy_ = bstack11111_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡣࡲ࡫ࡴࡢࡦࡤࡸࡦࠨᔵ")
    bstack1ll11l1l11l_opy_ = bstack11111_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨᔶ")
    bstack1ll11ll1l11_opy_ = bstack11111_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢᔷ")
    bstack1l111ll11ll_opy_ = bstack11111_opy_ (u"ࠢࡕࡇࡖࡘࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࠤᔸ")
    bstack1ll11lll11l_opy_ = bstack11111_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡌࡐࡉࠥᔹ")
    bstack1l11l1111ll_opy_ = bstack11111_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᔺ")
    bstack1lll1l1l1l1_opy_: Dict[str, bstack1lll1l1ll1l_opy_] = dict()
    bstack1l111111111_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll11llllll_opy_: List[str]
    bstack1ll1l11l111_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll11llllll_opy_: List[str],
        bstack1ll1l11l111_opy_: Dict[str, str],
        bstack1lll11l111l_opy_: bstack1lll111llll_opy_
    ):
        self.bstack1ll11llllll_opy_ = bstack1ll11llllll_opy_
        self.bstack1ll1l11l111_opy_ = bstack1ll1l11l111_opy_
        self.bstack1lll11l111l_opy_ = bstack1lll11l111l_opy_
    def track_event(
        self,
        context: bstack1ll1l11ll1l_opy_,
        test_framework_state: bstack1lll1ll111l_opy_,
        test_hook_state: bstack1lll1ll1l1l_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack11111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠥࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡿࠣࡥࡷ࡭ࡳ࠾ࡽࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࢃࠢᔻ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll11lllll1_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1lllll_opy_ = TestFramework.bstack1l1ll1l1ll1_opy_(bstack1llll11ll1l_opy_)
        if not bstack1l1ll1lllll_opy_ in TestFramework.bstack1l111111111_opy_:
            return
        self.logger.debug(bstack11111_opy_ (u"ࠦ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡻࡾࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࡷࠧᔼ").format(len(TestFramework.bstack1l111111111_opy_[bstack1l1ll1lllll_opy_])))
        for callback in TestFramework.bstack1l111111111_opy_[bstack1l1ll1lllll_opy_]:
            try:
                callback(self, instance, bstack1llll11ll1l_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack11111_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠧᔽ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1ll11l11l11_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll111lll11_opy_(self, instance, bstack1llll11ll1l_opy_):
        return
    @abc.abstractmethod
    def bstack1ll11111l11_opy_(self, instance, bstack1llll11ll1l_opy_):
        return
    @staticmethod
    def bstack1ll111llll1_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1l1lllll_opy_.create_context(target)
        instance = TestFramework.bstack1lll1l1l1l1_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1111l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l111ll1lll_opy_(reverse=True) -> List[bstack1lll1l1ll1l_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1lll1l1l1l1_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lll1ll1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11l11llll_opy_(ctx: bstack1lll1llllll_opy_, reverse=True) -> List[bstack1lll1l1ll1l_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1lll1l1l1l1_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lll1ll1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llllll1lll_opy_(instance: bstack1lll1l1ll1l_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1l1ll1l_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllllll11l_opy_(instance: bstack1lll1l1ll1l_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11111_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡽࠡ࡭ࡨࡽࡂࢁࡽࠡࡸࡤࡰࡺ࡫࠽ࡼࡿࠥᔾ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11l1ll1l_opy_(instance: bstack1lll1l1ll1l_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack11111_opy_ (u"ࠢࡴࡧࡷࡣࡸࡺࡡࡵࡧࡢࡩࡳࡺࡲࡪࡧࡶ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣࡩࡳࡺࡲࡪࡧࡶࡁࢀࢃࠢᔿ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack1l11111111l_opy_(instance: bstack1lll1ll111l_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11111_opy_ (u"ࠣࡷࡳࡨࡦࡺࡥࡠࡵࡷࡥࡹ࡫࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿࢂࠦ࡫ࡦࡻࡀࡿࢂࠦࡶࡢ࡮ࡸࡩࡂࢁࡽࠣᕀ").format(instance.ref(),key,value))
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
    def bstack1ll1111ll11_opy_(instance: bstack1lll1l1ll1l_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll11111lll_opy_(instance: bstack1lll1l1ll1l_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1ll1l1ll1_opy_(bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_]):
        return bstack11111_opy_ (u"ࠤ࠽ࠦᕁ").join((bstack1lll1ll111l_opy_(bstack1llll11ll1l_opy_[0]).name, bstack1lll1ll1l1l_opy_(bstack1llll11ll1l_opy_[1]).name))
    @staticmethod
    def bstack1llll11ll11_opy_(bstack1llll11ll1l_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1ll1l1l_opy_], callback: Callable):
        bstack1l1ll1lllll_opy_ = TestFramework.bstack1l1ll1l1ll1_opy_(bstack1llll11ll1l_opy_)
        TestFramework.logger.debug(bstack11111_opy_ (u"ࠥࡷࡪࡺ࡟ࡩࡱࡲ࡯ࡤࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡪࡲࡳࡰࡥࡲࡦࡩ࡬ࡷࡹࡸࡹࡠ࡭ࡨࡽࡂࢁࡽࠣᕂ").format(bstack1l1ll1lllll_opy_))
        if not bstack1l1ll1lllll_opy_ in TestFramework.bstack1l111111111_opy_:
            TestFramework.bstack1l111111111_opy_[bstack1l1ll1lllll_opy_] = []
        TestFramework.bstack1l111111111_opy_[bstack1l1ll1lllll_opy_].append(callback)
    @staticmethod
    def bstack1ll1l11ll11_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡶ࡬ࡲࡸࠨᕃ"):
            return klass.__qualname__
        return module + bstack11111_opy_ (u"ࠧ࠴ࠢᕄ") + klass.__qualname__
    @staticmethod
    def bstack1l1lllll11l_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}