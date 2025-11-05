# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import logging
from enum import Enum
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack1lll111llll_opy_ import bstack1lll11l111l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll11l1_opy_ import bstack1ll1ll11111_opy_, bstack1lll1lll1ll_opy_
class bstack1lll1ll1ll1_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11ll1ll_opy_ (u"ࠥࡘࡪࡹࡴࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᔘ").format(self.name)
class bstack1lll1l111l1_opy_(Enum):
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
        return bstack11ll1ll_opy_ (u"࡙ࠦ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᔙ").format(self.name)
class bstack1lll1l1l1ll_opy_(bstack1ll1ll11111_opy_):
    bstack1ll1l11111l_opy_: List[str]
    bstack1ll11ll1l11_opy_: Dict[str, str]
    state: bstack1lll1l111l1_opy_
    bstack1ll1llll1l1_opy_: datetime
    bstack1l1111111l1_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1lll1ll_opy_,
        bstack1ll1l11111l_opy_: List[str],
        bstack1ll11ll1l11_opy_: Dict[str, str],
        state=bstack1lll1l111l1_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll1l11111l_opy_ = bstack1ll1l11111l_opy_
        self.bstack1ll11ll1l11_opy_ = bstack1ll11ll1l11_opy_
        self.state = state
        self.bstack1ll1llll1l1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111111l1_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllllll1l1_opy_(self, bstack11llllllll1_opy_: bstack1lll1l111l1_opy_):
        bstack1l1111111ll_opy_ = bstack1lll1l111l1_opy_(bstack11llllllll1_opy_).name
        if not bstack1l1111111ll_opy_:
            return False
        if bstack11llllllll1_opy_ == self.state:
            return False
        self.state = bstack11llllllll1_opy_
        self.bstack1l1111111l1_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1ll1l111lll_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1l1llll111l_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1l1llllll1l_opy_: int = None
    bstack1ll111l11l1_opy_: str = None
    bstack1111lll_opy_: str = None
    bstack111lll111_opy_: str = None
    bstack1ll1l11ll11_opy_: str = None
    bstack1ll11l1l1ll_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll11llll1_opy_ = bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠣᔚ")
    bstack1ll1l11llll_opy_ = bstack11ll1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡮ࡪࠢᔛ")
    bstack1ll11ll11l1_opy_ = bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠥᔜ")
    bstack1ll1111l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡣࡵࡧࡴࡩࠤᔝ")
    bstack1ll111l111l_opy_ = bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡵࡣࡪࡷࠧᔞ")
    bstack1llll1111l1_opy_ = bstack11ll1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡴࡨࡷࡺࡲࡴࠣᔟ")
    bstack1l1lll1llll_opy_ = bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡸࡻ࡬ࡵࡡࡤࡸࠧᔠ")
    bstack1ll1l11ll1l_opy_ = bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᔡ")
    bstack1ll1l1l111l_opy_ = bstack11ll1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣࡪࡴࡤࡦࡦࡢࡥࡹࠨᔢ")
    bstack1l1llll11l1_opy_ = bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢᔣ")
    bstack1lll1ll11ll_opy_ = bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠢᔤ")
    bstack1lll11ll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠦᔥ")
    bstack1l1llll1111_opy_ = bstack11ll1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡥࡲࡨࡪࠨᔦ")
    bstack1ll111ll11l_opy_ = bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪࠨᔧ")
    bstack1llll1l11ll_opy_ = bstack11ll1ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࠨᔨ")
    bstack1lll1l1111l_opy_ = bstack11ll1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡧࡩ࡭ࡷࡵࡩࠧᔩ")
    bstack1ll1l11l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠦᔪ")
    bstack1ll111l1111_opy_ = bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥ࡬ࡰࡩࡶࠦᔫ")
    bstack1ll111ll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟࡮ࡧࡷࡥࠧᔬ")
    bstack1l11111111l_opy_ = bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡵࡦࡳࡵ࡫ࡳࠨᔭ")
    bstack1ll1lllll11_opy_ = bstack11ll1ll_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟࡯ࡣࡰࡩࠧᔮ")
    bstack1l1lllll1l1_opy_ = bstack11ll1ll_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᔯ")
    bstack1ll1l111ll1_opy_ = bstack11ll1ll_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᔰ")
    bstack1ll1l11l11l_opy_ = bstack11ll1ll_opy_ (u"ࠢࡩࡱࡲ࡯ࡤ࡯ࡤࠣᔱ")
    bstack1l1llll1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠣࡪࡲࡳࡰࡥࡲࡦࡵࡸࡰࡹࠨᔲ")
    bstack1ll11l1l111_opy_ = bstack11ll1ll_opy_ (u"ࠤ࡫ࡳࡴࡱ࡟࡭ࡱࡪࡷࠧᔳ")
    bstack1ll11111111_opy_ = bstack11ll1ll_opy_ (u"ࠥ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪࠨᔴ")
    bstack1ll1111ll11_opy_ = bstack11ll1ll_opy_ (u"ࠦࡱࡵࡧࡴࠤᔵ")
    bstack1ll1l111l1l_opy_ = bstack11ll1ll_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡤࡳࡥࡵࡣࡧࡥࡹࡧࠢᔶ")
    bstack1l1lll1lll1_opy_ = bstack11ll1ll_opy_ (u"ࠨࡰࡦࡰࡧ࡭ࡳ࡭ࠢᔷ")
    bstack1ll1111l11l_opy_ = bstack11ll1ll_opy_ (u"ࠢࡱࡧࡱࡨ࡮ࡴࡧࠣᔸ")
    bstack1l111ll1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࠥᔹ")
    bstack1ll11111lll_opy_ = bstack11ll1ll_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡍࡑࡊࠦᔺ")
    bstack1l11l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᔻ")
    bstack1llll111111_opy_: Dict[str, bstack1lll1l1l1ll_opy_] = dict()
    bstack1l111111111_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll1l11111l_opy_: List[str]
    bstack1ll11ll1l11_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll1l11111l_opy_: List[str],
        bstack1ll11ll1l11_opy_: Dict[str, str],
        bstack1lll111llll_opy_: bstack1lll11l111l_opy_
    ):
        self.bstack1ll1l11111l_opy_ = bstack1ll1l11111l_opy_
        self.bstack1ll11ll1l11_opy_ = bstack1ll11ll1l11_opy_
        self.bstack1lll111llll_opy_ = bstack1lll111llll_opy_
    def track_event(
        self,
        context: bstack1ll1l111lll_opy_,
        test_framework_state: bstack1lll1l111l1_opy_,
        test_hook_state: bstack1lll1ll1ll1_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠤࡦࡸࡧࡴ࠿ࡾࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁࡽࠣᔼ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1ll11l1lll1_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1ll1llll1_opy_ = TestFramework.bstack1l1ll1l111l_opy_(bstack1lllllllll1_opy_)
        if not bstack1l1ll1llll1_opy_ in TestFramework.bstack1l111111111_opy_:
            return
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠧ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡼࡿࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࡸࠨᔽ").format(len(TestFramework.bstack1l111111111_opy_[bstack1l1ll1llll1_opy_])))
        for callback in TestFramework.bstack1l111111111_opy_[bstack1l1ll1llll1_opy_]:
            try:
                callback(self, instance, bstack1lllllllll1_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack11ll1ll_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࡿࢂࠨᔾ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1l1lllll111_opy_(self):
        return
    @abc.abstractmethod
    def bstack1ll11l111ll_opy_(self, instance, bstack1lllllllll1_opy_):
        return
    @abc.abstractmethod
    def bstack1ll11lll1ll_opy_(self, instance, bstack1lllllllll1_opy_):
        return
    @staticmethod
    def bstack1ll11l1ll11_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1ll1ll11111_opy_.create_context(target)
        instance = TestFramework.bstack1llll111111_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1l1lllll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1ll11l_opy_(reverse=True) -> List[bstack1lll1l1l1ll_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1llll111111_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1llll1l1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1l11l11l1ll_opy_(ctx: bstack1lll1lll1ll_opy_, reverse=True) -> List[bstack1lll1l1l1ll_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1llll111111_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1llll1l1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllll1llll_opy_(instance: bstack1lll1l1l1ll_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lll1l1l1ll_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllllll1l1_opy_(instance: bstack1lll1l1l1ll_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡴࡧࡷࡣࡸࡺࡡࡵࡧ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢ࡮ࡩࡾࡃࡻࡾࠢࡹࡥࡱࡻࡥ࠾ࡽࢀࠦᔿ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11ll1l1l_opy_(instance: bstack1lll1l1l1ll_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡵࡨࡸࡤࡹࡴࡢࡶࡨࡣࡪࡴࡴࡳ࡫ࡨࡷ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽࢀࠤࡪࡴࡴࡳ࡫ࡨࡷࡂࢁࡽࠣᕀ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack11lllllllll_opy_(instance: bstack1lll1l111l1_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡸࡴࡩࡧࡴࡦࡡࡶࡸࡦࡺࡥ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡬ࡧࡼࡁࢀࢃࠠࡷࡣ࡯ࡹࡪࡃࡻࡾࠤᕁ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1ll11l1ll11_opy_(target, strict)
        return TestFramework.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1ll11l1ll11_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1ll11ll11ll_opy_(instance: bstack1lll1l1l1ll_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1ll11lllll1_opy_(instance: bstack1lll1l1l1ll_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l1ll1l111l_opy_(bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_]):
        return bstack11ll1ll_opy_ (u"ࠥ࠾ࠧᕂ").join((bstack1lll1l111l1_opy_(bstack1lllllllll1_opy_[0]).name, bstack1lll1ll1ll1_opy_(bstack1lllllllll1_opy_[1]).name))
    @staticmethod
    def bstack1lllll1l11l_opy_(bstack1lllllllll1_opy_: Tuple[bstack1lll1l111l1_opy_, bstack1lll1ll1ll1_opy_], callback: Callable):
        bstack1l1ll1llll1_opy_ = TestFramework.bstack1l1ll1l111l_opy_(bstack1lllllllll1_opy_)
        TestFramework.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡸ࡫ࡴࡠࡪࡲࡳࡰࡥࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢ࡫ࡳࡴࡱ࡟ࡳࡧࡪ࡭ࡸࡺࡲࡺࡡ࡮ࡩࡾࡃࡻࡾࠤᕃ").format(bstack1l1ll1llll1_opy_))
        if not bstack1l1ll1llll1_opy_ in TestFramework.bstack1l111111111_opy_:
            TestFramework.bstack1l111111111_opy_[bstack1l1ll1llll1_opy_] = []
        TestFramework.bstack1l111111111_opy_[bstack1l1ll1llll1_opy_].append(callback)
    @staticmethod
    def bstack1ll1l11lll1_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡷ࡭ࡳࡹࠢᕄ"):
            return klass.__qualname__
        return module + bstack11ll1ll_opy_ (u"ࠨ࠮ࠣᕅ") + klass.__qualname__
    @staticmethod
    def bstack1l1llll1lll_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}