# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1ll1llllll1_opy_ import bstack1ll1ll11ll1_opy_, bstack1llll111111_opy_
import os
import threading
class bstack1llll1l111l_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l1_opy_ (u"ࠢࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᔜ").format(self.name)
class bstack1llllll111l_opy_(Enum):
    NONE = 0
    bstack1lllll1ll11_opy_ = 1
    bstack1ll1lll1l11_opy_ = 3
    bstack1lllllll111_opy_ = 4
    bstack1l1111111l1_opy_ = 5
    QUIT = 6
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack1l1_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡣࡷࡩ࠳ࢁࡽࠣᔝ").format(self.name)
class bstack1llllll1l1l_opy_(bstack1ll1ll11ll1_opy_):
    framework_name: str
    framework_version: str
    state: bstack1llllll111l_opy_
    previous_state: bstack1llllll111l_opy_
    bstack1ll1llll1l1_opy_: datetime
    bstack1l11111ll1l_opy_: datetime
    def __init__(
        self,
        context: bstack1llll111111_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1llllll111l_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1llllll111l_opy_.NONE
        self.bstack1ll1llll1l1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l11111ll1l_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll1l1lll_opy_(self, bstack1l11111l1l1_opy_: bstack1llllll111l_opy_):
        bstack1l11111lll1_opy_ = bstack1llllll111l_opy_(bstack1l11111l1l1_opy_).name
        if not bstack1l11111lll1_opy_:
            return False
        if bstack1l11111l1l1_opy_ == self.state:
            return False
        if self.state == bstack1llllll111l_opy_.bstack1ll1lll1l11_opy_: # bstack1l111111l11_opy_ bstack1l111111111_opy_ for bstack11lllllll11_opy_ in Playwright, it bstack11llllll1ll_opy_ bstack11lllllllll_opy_ multiple times bstack1l111111ll1_opy_ a new state
            return True
        if (
            bstack1l11111l1l1_opy_ == bstack1llllll111l_opy_.NONE
            or (self.state != bstack1llllll111l_opy_.NONE and bstack1l11111l1l1_opy_ == bstack1llllll111l_opy_.bstack1lllll1ll11_opy_)
            or (self.state < bstack1llllll111l_opy_.bstack1lllll1ll11_opy_ and bstack1l11111l1l1_opy_ == bstack1llllll111l_opy_.bstack1lllllll111_opy_)
            or (self.state < bstack1llllll111l_opy_.bstack1lllll1ll11_opy_ and bstack1l11111l1l1_opy_ == bstack1llllll111l_opy_.QUIT)
        ):
            raise ValueError(bstack1l1_opy_ (u"ࠤ࡬ࡲࡻࡧ࡬ࡪࡦࠣࡷࡹࡧࡴࡦࠢࡷࡶࡦࡴࡳࡪࡶ࡬ࡳࡳࡀࠠࠣᔞ") + str(self.state) + bstack1l1_opy_ (u"ࠥࠤࡂࡄࠠࠣᔟ") + str(bstack1l11111l1l1_opy_))
        self.previous_state = self.state
        self.state = bstack1l11111l1l1_opy_
        self.bstack1l11111ll1l_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll11111ll_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1lllll1_opy_: Dict[str, bstack1llllll1l1l_opy_] = dict()
    framework_name: str
    framework_version: str
    classes: List[Type]
    def __init__(
        self,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
    ):
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.classes = classes
    @abc.abstractmethod
    def bstack1l1lll1ll1l_opy_(self, instance: bstack1llllll1l1l_opy_, method_name: str, bstack1l1ll1ll111_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1lll11l1l_opy_(
        self, method_name, previous_state: bstack1llllll111l_opy_, *args, **kwargs
    ) -> bstack1llllll111l_opy_:
        return
    @abc.abstractmethod
    def bstack1l1ll1lllll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1lll1l111_opy_(self, bstack11llllllll1_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack11llllllll1_opy_:
                bstack1l11111111l_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1l11111111l_opy_):
                    self.logger.warning(bstack1l1_opy_ (u"ࠦࡺࡴࡰࡢࡶࡦ࡬ࡪࡪࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࠤᔠ") + str(method_name) + bstack1l1_opy_ (u"ࠧࠨᔡ"))
                    continue
                bstack1l1ll1ll1ll_opy_ = self.bstack1l1lll11l1l_opy_(
                    method_name, previous_state=bstack1llllll111l_opy_.NONE
                )
                bstack1l11111l111_opy_ = self.bstack11lllllll1l_opy_(
                    method_name,
                    (bstack1l1ll1ll1ll_opy_ if bstack1l1ll1ll1ll_opy_ else bstack1llllll111l_opy_.NONE),
                    bstack1l11111111l_opy_,
                )
                if not callable(bstack1l11111l111_opy_):
                    self.logger.warning(bstack1l1_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠦ࡮ࡰࡶࠣࡴࡦࡺࡣࡩࡧࡧ࠾ࠥࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࠮ࡻࡴࡧ࡯ࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃ࠺ࠡࠤᔢ") + str(self.framework_version) + bstack1l1_opy_ (u"ࠢࠪࠤᔣ"))
                    continue
                setattr(clazz, method_name, bstack1l11111l111_opy_)
    def bstack11lllllll1l_opy_(
        self,
        method_name: str,
        bstack1l1ll1ll1ll_opy_: bstack1llllll111l_opy_,
        bstack1l11111111l_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1l1ll111l_opy_ = datetime.now()
            (bstack1l1ll1ll1ll_opy_,) = wrapped.__vars__
            bstack1l1ll1ll1ll_opy_ = (
                bstack1l1ll1ll1ll_opy_
                if bstack1l1ll1ll1ll_opy_ and bstack1l1ll1ll1ll_opy_ != bstack1llllll111l_opy_.NONE
                else self.bstack1l1lll11l1l_opy_(method_name, previous_state=bstack1l1ll1ll1ll_opy_, *args, **kwargs)
            )
            if bstack1l1ll1ll1ll_opy_ == bstack1llllll111l_opy_.bstack1lllll1ll11_opy_:
                ctx = bstack1ll1ll11ll1_opy_.create_context(self.bstack11llllll1l1_opy_(target))
                if not self.bstack1l111111l1l_opy_() or ctx.id not in bstack1lll11111ll_opy_.bstack1lll1lllll1_opy_:
                    bstack1lll11111ll_opy_.bstack1lll1lllll1_opy_[ctx.id] = bstack1llllll1l1l_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1ll1ll1ll_opy_
                    )
                self.logger.debug(bstack1l1_opy_ (u"ࠣࡹࡵࡥࡵࡶࡥࡥࠢࡰࡩࡹ࡮࡯ࡥࠢࡦࡶࡪࡧࡴࡦࡦ࠽ࠤࢀࡺࡡࡳࡩࡨࡸ࠳ࡥ࡟ࡤ࡮ࡤࡷࡸࡥ࡟ࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡣࡵࡺࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᔤ") + str(bstack1lll11111ll_opy_.bstack1lll1lllll1_opy_.keys()) + bstack1l1_opy_ (u"ࠤࠥᔥ"))
            else:
                self.logger.debug(bstack1l1_opy_ (u"ࠥࡻࡷࡧࡰࡱࡧࡧࠤࡲ࡫ࡴࡩࡱࡧࠤ࡮ࡴࡶࡰ࡭ࡨࡨ࠿ࠦࡻࡵࡣࡵ࡫ࡪࡺ࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧᔦ") + str(bstack1lll11111ll_opy_.bstack1lll1lllll1_opy_.keys()) + bstack1l1_opy_ (u"ࠦࠧᔧ"))
            instance = bstack1lll11111ll_opy_.bstack1ll1l11l1l1_opy_(self.bstack11llllll1l1_opy_(target))
            if bstack1l1ll1ll1ll_opy_ == bstack1llllll111l_opy_.NONE or not instance:
                ctx = bstack1ll1ll11ll1_opy_.create_context(self.bstack11llllll1l1_opy_(target))
                self.logger.warning(bstack1l1_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡵ࡯ࡶࡵࡥࡨࡱࡥࡥ࠼ࠣࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡦࡸࡽࡃࡻࡤࡶࡻࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᔨ") + str(bstack1lll11111ll_opy_.bstack1lll1lllll1_opy_.keys()) + bstack1l1_opy_ (u"ࠨࠢᔩ"))
                return bstack1l11111111l_opy_(target, *args, **kwargs)
            bstack1l1ll11lll1_opy_ = self.bstack1l1ll1lllll_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1ll1ll_opy_, bstack1llll1l111l_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1llll1l1lll_opy_(bstack1l1ll1ll1ll_opy_):
                self.logger.debug(bstack1l1_opy_ (u"ࠢࡢࡲࡳࡰ࡮࡫ࡤࠡࡵࡷࡥࡹ࡫࠭ࡵࡴࡤࡲࡸ࡯ࡴࡪࡱࡱ࠾ࠥࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡲࡵࡩࡻ࡯࡯ࡶࡵࡢࡷࡹࡧࡴࡦࡿࠣࡁࡃࠦࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡶࡸࡦࡺࡥࡾࠢࠫࡿࡹࡿࡰࡦࠪࡷࡥࡷ࡭ࡥࡵࠫࢀ࠲ࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤࢀࡧࡲࡨࡵࢀ࠭ࠥࡡࠢᔪ") + str(instance.ref()) + bstack1l1_opy_ (u"ࠣ࡟ࠥᔫ"))
            result = (
                bstack1l1ll11lll1_opy_(target, bstack1l11111111l_opy_, *args, **kwargs)
                if callable(bstack1l1ll11lll1_opy_)
                else bstack1l11111111l_opy_(target, *args, **kwargs)
            )
            bstack1l111111lll_opy_ = self.bstack1l1ll1lllll_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1ll1ll_opy_, bstack1llll1l111l_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1lll1ll1l_opy_(instance, method_name, datetime.now() - bstack1l1ll111l_opy_, *args, **kwargs)
            return bstack1l111111lll_opy_ if bstack1l111111lll_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1ll1ll1ll_opy_,)
        return wrapped
    @staticmethod
    def bstack1ll1l11l1l1_opy_(target: object, strict=True):
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        instance = bstack1lll11111ll_opy_.bstack1lll1lllll1_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1l111_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1lll1l_opy_(
        ctx: bstack1llll111111_opy_, state: bstack1llllll111l_opy_, reverse=True
    ) -> List[bstack1llllll1l1l_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll11111ll_opy_.bstack1lll1lllll1_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1llll1l1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llllllll11_opy_(instance: bstack1llllll1l1l_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llllll1l1l_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll1l1lll_opy_(instance: bstack1llllll1l1l_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll11111ll_opy_.logger.debug(bstack1l1_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡰ࡫ࡹ࠾ࡽ࡮ࡩࡾࢃࠠࡷࡣ࡯ࡹࡪࡃࠢᔬ") + str(value) + bstack1l1_opy_ (u"ࠥࠦᔭ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll11111ll_opy_.bstack1ll1l11l1l1_opy_(target, strict)
        return bstack1lll11111ll_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll11111ll_opy_.bstack1ll1l11l1l1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack1l111111l1l_opy_(self):
        return self.framework_name == bstack1l1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᔮ")
    def bstack11llllll1l1_opy_(self, target):
        return target if not self.bstack1l111111l1l_opy_() else self.bstack1l1111111ll_opy_()
    @staticmethod
    def bstack1l1111111ll_opy_():
        return str(os.getpid()) + str(threading.get_ident())