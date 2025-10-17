# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1lll1111l11_opy_ import bstack1ll1ll1ll1l_opy_, bstack1lll1lll1l1_opy_
import os
import threading
class bstack1llllllll1l_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l111_opy_ (u"ࠦࡍࡵ࡯࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥᓶ").format(self.name)
class bstack1lllll11111_opy_(Enum):
    NONE = 0
    bstack1lllll11lll_opy_ = 1
    bstack1ll1ll1llll_opy_ = 3
    bstack1llll1lllll_opy_ = 4
    bstack1l1111111ll_opy_ = 5
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
        return bstack11l111_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᓷ").format(self.name)
class bstack1llllll1lll_opy_(bstack1ll1ll1ll1l_opy_):
    framework_name: str
    framework_version: str
    state: bstack1lllll11111_opy_
    previous_state: bstack1lllll11111_opy_
    bstack1ll1llllll1_opy_: datetime
    bstack1l1111l11ll_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1lll1l1_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1lllll11111_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1lllll11111_opy_.NONE
        self.bstack1ll1llllll1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll111ll_opy_(self, bstack1l1111l1111_opy_: bstack1lllll11111_opy_):
        bstack1l1111l11l1_opy_ = bstack1lllll11111_opy_(bstack1l1111l1111_opy_).name
        if not bstack1l1111l11l1_opy_:
            return False
        if bstack1l1111l1111_opy_ == self.state:
            return False
        if self.state == bstack1lllll11111_opy_.bstack1ll1ll1llll_opy_: # bstack1l11111111l_opy_ bstack1l111111l1l_opy_ for bstack1l11111l1ll_opy_ in Playwright, it bstack1l111111lll_opy_ bstack1l11111l1l1_opy_ multiple times bstack1l111111l11_opy_ a new state
            return True
        if (
            bstack1l1111l1111_opy_ == bstack1lllll11111_opy_.NONE
            or (self.state != bstack1lllll11111_opy_.NONE and bstack1l1111l1111_opy_ == bstack1lllll11111_opy_.bstack1lllll11lll_opy_)
            or (self.state < bstack1lllll11111_opy_.bstack1lllll11lll_opy_ and bstack1l1111l1111_opy_ == bstack1lllll11111_opy_.bstack1llll1lllll_opy_)
            or (self.state < bstack1lllll11111_opy_.bstack1lllll11lll_opy_ and bstack1l1111l1111_opy_ == bstack1lllll11111_opy_.QUIT)
        ):
            raise ValueError(bstack11l111_opy_ (u"ࠨࡩ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡶࡤࡸࡪࠦࡴࡳࡣࡱࡷ࡮ࡺࡩࡰࡰ࠽ࠤࠧᓸ") + str(self.state) + bstack11l111_opy_ (u"ࠢࠡ࠿ࡁࠤࠧᓹ") + str(bstack1l1111l1111_opy_))
        self.previous_state = self.state
        self.state = bstack1l1111l1111_opy_
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll11ll11l_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1l11lll_opy_: Dict[str, bstack1llllll1lll_opy_] = dict()
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
    def bstack1l1ll1ll1ll_opy_(self, instance: bstack1llllll1lll_opy_, method_name: str, bstack1l1lll11111_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1lll1ll11_opy_(
        self, method_name, previous_state: bstack1lllll11111_opy_, *args, **kwargs
    ) -> bstack1lllll11111_opy_:
        return
    @abc.abstractmethod
    def bstack1l1lll1l111_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1ll1lllll_opy_(self, bstack1l111111ll1_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack1l111111ll1_opy_:
                bstack1l11111l11l_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1l11111l11l_opy_):
                    self.logger.warning(bstack11l111_opy_ (u"ࠣࡷࡱࡴࡦࡺࡣࡩࡧࡧࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠥࠨᓺ") + str(method_name) + bstack11l111_opy_ (u"ࠤࠥᓻ"))
                    continue
                bstack1l1llll1111_opy_ = self.bstack1l1lll1ll11_opy_(
                    method_name, previous_state=bstack1lllll11111_opy_.NONE
                )
                bstack1l11111l111_opy_ = self.bstack1l11111ll1l_opy_(
                    method_name,
                    (bstack1l1llll1111_opy_ if bstack1l1llll1111_opy_ else bstack1lllll11111_opy_.NONE),
                    bstack1l11111l11l_opy_,
                )
                if not callable(bstack1l11111l111_opy_):
                    self.logger.warning(bstack11l111_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠣࡲࡴࡺࠠࡱࡣࡷࡧ࡭࡫ࡤ࠻ࠢࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࠫࡿࡸ࡫࡬ࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀ࠾ࠥࠨᓼ") + str(self.framework_version) + bstack11l111_opy_ (u"ࠦ࠮ࠨᓽ"))
                    continue
                setattr(clazz, method_name, bstack1l11111l111_opy_)
    def bstack1l11111ll1l_opy_(
        self,
        method_name: str,
        bstack1l1llll1111_opy_: bstack1lllll11111_opy_,
        bstack1l11111l11l_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1lll1l1ll1_opy_ = datetime.now()
            (bstack1l1llll1111_opy_,) = wrapped.__vars__
            bstack1l1llll1111_opy_ = (
                bstack1l1llll1111_opy_
                if bstack1l1llll1111_opy_ and bstack1l1llll1111_opy_ != bstack1lllll11111_opy_.NONE
                else self.bstack1l1lll1ll11_opy_(method_name, previous_state=bstack1l1llll1111_opy_, *args, **kwargs)
            )
            if bstack1l1llll1111_opy_ == bstack1lllll11111_opy_.bstack1lllll11lll_opy_:
                ctx = bstack1ll1ll1ll1l_opy_.create_context(self.bstack1l11111ll11_opy_(target))
                if not self.bstack11lllllllll_opy_() or ctx.id not in bstack1lll11ll11l_opy_.bstack1lll1l11lll_opy_:
                    bstack1lll11ll11l_opy_.bstack1lll1l11lll_opy_[ctx.id] = bstack1llllll1lll_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1llll1111_opy_
                    )
                self.logger.debug(bstack11l111_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡣࡳࡧࡤࡸࡪࡪ࠺ࠡࡽࡷࡥࡷ࡭ࡥࡵ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡧࡹࡾ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨᓾ") + str(bstack1lll11ll11l_opy_.bstack1lll1l11lll_opy_.keys()) + bstack11l111_opy_ (u"ࠨࠢᓿ"))
            else:
                self.logger.debug(bstack11l111_opy_ (u"ࠢࡸࡴࡤࡴࡵ࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤࠡ࡫ࡱࡺࡴࡱࡥࡥ࠼ࠣࡿࡹࡧࡲࡨࡧࡷ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᔀ") + str(bstack1lll11ll11l_opy_.bstack1lll1l11lll_opy_.keys()) + bstack11l111_opy_ (u"ࠣࠤᔁ"))
            instance = bstack1lll11ll11l_opy_.bstack1ll111llll1_opy_(self.bstack1l11111ll11_opy_(target))
            if bstack1l1llll1111_opy_ == bstack1lllll11111_opy_.NONE or not instance:
                ctx = bstack1ll1ll1ll1l_opy_.create_context(self.bstack1l11111ll11_opy_(target))
                self.logger.warning(bstack11l111_opy_ (u"ࠤࡺࡶࡦࡶࡰࡦࡦࠣࡱࡪࡺࡨࡰࡦࠣࡹࡳࡺࡲࡢࡥ࡮ࡩࡩࡀࠠࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡣࡵࡺࡀࡿࡨࡺࡸࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨᔂ") + str(bstack1lll11ll11l_opy_.bstack1lll1l11lll_opy_.keys()) + bstack11l111_opy_ (u"ࠥࠦᔃ"))
                return bstack1l11111l11l_opy_(target, *args, **kwargs)
            bstack1l1ll11ll1l_opy_ = self.bstack1l1lll1l111_opy_(
                target,
                (instance, method_name),
                (bstack1l1llll1111_opy_, bstack1llllllll1l_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1lllll111ll_opy_(bstack1l1llll1111_opy_):
                self.logger.debug(bstack11l111_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡨࡨࠥࡹࡴࡢࡶࡨ࠱ࡹࡸࡡ࡯ࡵ࡬ࡸ࡮ࡵ࡮࠻ࠢࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡶࡲࡦࡸ࡬ࡳࡺࡹ࡟ࡴࡶࡤࡸࡪࢃࠠ࠾ࡀࠣࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡳࡵࡣࡷࡩࢂࠦࠨࡼࡶࡼࡴࡪ࠮ࡴࡢࡴࡪࡩࡹ࠯ࡽ࠯ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡽࡤࡶ࡬ࡹࡽࠪࠢ࡞ࠦᔄ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠧࡣࠢᔅ"))
            result = (
                bstack1l1ll11ll1l_opy_(target, bstack1l11111l11l_opy_, *args, **kwargs)
                if callable(bstack1l1ll11ll1l_opy_)
                else bstack1l11111l11l_opy_(target, *args, **kwargs)
            )
            bstack1l1111111l1_opy_ = self.bstack1l1lll1l111_opy_(
                target,
                (instance, method_name),
                (bstack1l1llll1111_opy_, bstack1llllllll1l_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1ll1ll1ll_opy_(instance, method_name, datetime.now() - bstack1lll1l1ll1_opy_, *args, **kwargs)
            return bstack1l1111111l1_opy_ if bstack1l1111111l1_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1llll1111_opy_,)
        return wrapped
    @staticmethod
    def bstack1ll111llll1_opy_(target: object, strict=True):
        ctx = bstack1ll1ll1ll1l_opy_.create_context(target)
        instance = bstack1lll11ll11l_opy_.bstack1lll1l11lll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1l1ll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l11l1ll_opy_(
        ctx: bstack1lll1lll1l1_opy_, state: bstack1lllll11111_opy_, reverse=True
    ) -> List[bstack1llllll1lll_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll11ll11l_opy_.bstack1lll1l11lll_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1llllll1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllll11l1l_opy_(instance: bstack1llllll1lll_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llllll1lll_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll111ll_opy_(instance: bstack1llllll1lll_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll11ll11l_opy_.logger.debug(bstack11l111_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡ࡭ࡨࡽࡂࢁ࡫ࡦࡻࢀࠤࡻࡧ࡬ࡶࡧࡀࠦᔆ") + str(value) + bstack11l111_opy_ (u"ࠢࠣᔇ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll11ll11l_opy_.bstack1ll111llll1_opy_(target, strict)
        return bstack1lll11ll11l_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll11ll11l_opy_.bstack1ll111llll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack11lllllllll_opy_(self):
        return self.framework_name == bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᔈ")
    def bstack1l11111ll11_opy_(self, target):
        return target if not self.bstack11lllllllll_opy_() else self.bstack1l111111111_opy_()
    @staticmethod
    def bstack1l111111111_opy_():
        return str(os.getpid()) + str(threading.get_ident())