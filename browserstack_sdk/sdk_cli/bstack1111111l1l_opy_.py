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
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1ll1ll1llll_opy_, bstack1llll11l111_opy_
import os
import threading
class bstack1llllll1ll1_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l_opy_ (u"ࠤࡋࡳࡴࡱࡓࡵࡣࡷࡩ࠳ࢁࡽࠣᔉ").format(self.name)
class bstack1111111l11_opy_(Enum):
    NONE = 0
    bstack1llllll1l1l_opy_ = 1
    bstack1ll1llll111_opy_ = 3
    bstack1111111ll1_opy_ = 4
    bstack1l11111ll1l_opy_ = 5
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
        return bstack1l_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥᔊ").format(self.name)
class bstack111111l111_opy_(bstack1ll1ll1llll_opy_):
    framework_name: str
    framework_version: str
    state: bstack1111111l11_opy_
    previous_state: bstack1111111l11_opy_
    bstack1lll11111ll_opy_: datetime
    bstack1l1111l1lll_opy_: datetime
    def __init__(
        self,
        context: bstack1llll11l111_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1111111l11_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1111111l11_opy_.NONE
        self.bstack1lll11111ll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l1lll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll11ll1_opy_(self, bstack1l1111l1ll1_opy_: bstack1111111l11_opy_):
        bstack1l1111l1l11_opy_ = bstack1111111l11_opy_(bstack1l1111l1ll1_opy_).name
        if not bstack1l1111l1l11_opy_:
            return False
        if bstack1l1111l1ll1_opy_ == self.state:
            return False
        if self.state == bstack1111111l11_opy_.bstack1ll1llll111_opy_: # bstack1l111111l1l_opy_ bstack1l11111lll1_opy_ for bstack1l1111l111l_opy_ in Playwright, it bstack1l11111l111_opy_ bstack1l11111l1l1_opy_ multiple times bstack1l1111111ll_opy_ a new state
            return True
        if (
            bstack1l1111l1ll1_opy_ == bstack1111111l11_opy_.NONE
            or (self.state != bstack1111111l11_opy_.NONE and bstack1l1111l1ll1_opy_ == bstack1111111l11_opy_.bstack1llllll1l1l_opy_)
            or (self.state < bstack1111111l11_opy_.bstack1llllll1l1l_opy_ and bstack1l1111l1ll1_opy_ == bstack1111111l11_opy_.bstack1111111ll1_opy_)
            or (self.state < bstack1111111l11_opy_.bstack1llllll1l1l_opy_ and bstack1l1111l1ll1_opy_ == bstack1111111l11_opy_.QUIT)
        ):
            raise ValueError(bstack1l_opy_ (u"ࠦ࡮ࡴࡶࡢ࡮࡬ࡨࠥࡹࡴࡢࡶࡨࠤࡹࡸࡡ࡯ࡵ࡬ࡸ࡮ࡵ࡮࠻ࠢࠥᔋ") + str(self.state) + bstack1l_opy_ (u"ࠧࠦ࠽࠿ࠢࠥᔌ") + str(bstack1l1111l1ll1_opy_))
        self.previous_state = self.state
        self.state = bstack1l1111l1ll1_opy_
        self.bstack1l1111l1lll_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll111llll_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llll11l1ll_opy_: Dict[str, bstack111111l111_opy_] = dict()
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
    def bstack1l1ll1lllll_opy_(self, instance: bstack111111l111_opy_, method_name: str, bstack1l1lll1l1l1_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1lll111ll_opy_(
        self, method_name, previous_state: bstack1111111l11_opy_, *args, **kwargs
    ) -> bstack1111111l11_opy_:
        return
    @abc.abstractmethod
    def bstack1l1lll1ll1l_opy_(
        self,
        target: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1lll1l111_opy_(self, bstack1l11111ll11_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack1l11111ll11_opy_:
                bstack1l1111l1111_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1l1111l1111_opy_):
                    self.logger.warning(bstack1l_opy_ (u"ࠨࡵ࡯ࡲࡤࡸࡨ࡮ࡥࡥࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࠦᔍ") + str(method_name) + bstack1l_opy_ (u"ࠢࠣᔎ"))
                    continue
                bstack1l1lll1lll1_opy_ = self.bstack1l1lll111ll_opy_(
                    method_name, previous_state=bstack1111111l11_opy_.NONE
                )
                bstack1l111111ll1_opy_ = self.bstack1l111111l11_opy_(
                    method_name,
                    (bstack1l1lll1lll1_opy_ if bstack1l1lll1lll1_opy_ else bstack1111111l11_opy_.NONE),
                    bstack1l1111l1111_opy_,
                )
                if not callable(bstack1l111111ll1_opy_):
                    self.logger.warning(bstack1l_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࠡࡰࡲࡸࠥࡶࡡࡵࡥ࡫ࡩࡩࡀࠠࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࠩࡽࡶࡩࡱ࡬࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾ࠼ࠣࠦᔏ") + str(self.framework_version) + bstack1l_opy_ (u"ࠤࠬࠦᔐ"))
                    continue
                setattr(clazz, method_name, bstack1l111111ll1_opy_)
    def bstack1l111111l11_opy_(
        self,
        method_name: str,
        bstack1l1lll1lll1_opy_: bstack1111111l11_opy_,
        bstack1l1111l1111_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1l1111lll_opy_ = datetime.now()
            (bstack1l1lll1lll1_opy_,) = wrapped.__vars__
            bstack1l1lll1lll1_opy_ = (
                bstack1l1lll1lll1_opy_
                if bstack1l1lll1lll1_opy_ and bstack1l1lll1lll1_opy_ != bstack1111111l11_opy_.NONE
                else self.bstack1l1lll111ll_opy_(method_name, previous_state=bstack1l1lll1lll1_opy_, *args, **kwargs)
            )
            if bstack1l1lll1lll1_opy_ == bstack1111111l11_opy_.bstack1llllll1l1l_opy_:
                ctx = bstack1ll1ll1llll_opy_.create_context(self.bstack1l111111lll_opy_(target))
                if not self.bstack1l11111l11l_opy_() or ctx.id not in bstack1lll111llll_opy_.bstack1llll11l1ll_opy_:
                    bstack1lll111llll_opy_.bstack1llll11l1ll_opy_[ctx.id] = bstack111111l111_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1lll1lll1_opy_
                    )
                self.logger.debug(bstack1l_opy_ (u"ࠥࡻࡷࡧࡰࡱࡧࡧࠤࡲ࡫ࡴࡩࡱࡧࠤࡨࡸࡥࡢࡶࡨࡨ࠿ࠦࡻࡵࡣࡵ࡫ࡪࡺ࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡥࡷࡼࡂࢁࡣࡵࡺ࠱࡭ࡩࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦᔑ") + str(bstack1lll111llll_opy_.bstack1llll11l1ll_opy_.keys()) + bstack1l_opy_ (u"ࠦࠧᔒ"))
            else:
                self.logger.debug(bstack1l_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡩ࡯ࡸࡲ࡯ࡪࡪ࠺ࠡࡽࡷࡥࡷ࡭ࡥࡵ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡸࡃࠢᔓ") + str(bstack1lll111llll_opy_.bstack1llll11l1ll_opy_.keys()) + bstack1l_opy_ (u"ࠨࠢᔔ"))
            instance = bstack1lll111llll_opy_.bstack1ll11ll1ll1_opy_(self.bstack1l111111lll_opy_(target))
            if bstack1l1lll1lll1_opy_ == bstack1111111l11_opy_.NONE or not instance:
                ctx = bstack1ll1ll1llll_opy_.create_context(self.bstack1l111111lll_opy_(target))
                self.logger.warning(bstack1l_opy_ (u"ࠢࡸࡴࡤࡴࡵ࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤࠡࡷࡱࡸࡷࡧࡣ࡬ࡧࡧ࠾ࠥࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡨࡺࡸ࠾ࡽࡦࡸࡽࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦᔕ") + str(bstack1lll111llll_opy_.bstack1llll11l1ll_opy_.keys()) + bstack1l_opy_ (u"ࠣࠤᔖ"))
                return bstack1l1111l1111_opy_(target, *args, **kwargs)
            bstack1l1ll1l1l11_opy_ = self.bstack1l1lll1ll1l_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll1lll1_opy_, bstack1llllll1ll1_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1lllll11ll1_opy_(bstack1l1lll1lll1_opy_):
                self.logger.debug(bstack1l_opy_ (u"ࠤࡤࡴࡵࡲࡩࡦࡦࠣࡷࡹࡧࡴࡦ࠯ࡷࡶࡦࡴࡳࡪࡶ࡬ࡳࡳࡀࠠࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡴࡷ࡫ࡶࡪࡱࡸࡷࡤࡹࡴࡢࡶࡨࢁࠥࡃ࠾ࠡࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡸࡺࡡࡵࡧࢀࠤ࠭ࢁࡴࡺࡲࡨࠬࡹࡧࡲࡨࡧࡷ࠭ࢂ࠴ࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡻࡢࡴࡪࡷࢂ࠯ࠠ࡜ࠤᔗ") + str(instance.ref()) + bstack1l_opy_ (u"ࠥࡡࠧᔘ"))
            result = (
                bstack1l1ll1l1l11_opy_(target, bstack1l1111l1111_opy_, *args, **kwargs)
                if callable(bstack1l1ll1l1l11_opy_)
                else bstack1l1111l1111_opy_(target, *args, **kwargs)
            )
            bstack1l11111l1ll_opy_ = self.bstack1l1lll1ll1l_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll1lll1_opy_, bstack1llllll1ll1_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1ll1lllll_opy_(instance, method_name, datetime.now() - bstack1l1111lll_opy_, *args, **kwargs)
            return bstack1l11111l1ll_opy_ if bstack1l11111l1ll_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1lll1lll1_opy_,)
        return wrapped
    @staticmethod
    def bstack1ll11ll1ll1_opy_(target: object, strict=True):
        ctx = bstack1ll1ll1llll_opy_.create_context(target)
        instance = bstack1lll111llll_opy_.bstack1llll11l1ll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1lll111l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11ll111ll_opy_(
        ctx: bstack1llll11l111_opy_, state: bstack1111111l11_opy_, reverse=True
    ) -> List[bstack111111l111_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll111llll_opy_.bstack1llll11l1ll_opy_.values(),
            ),
            key=lambda t: t.bstack1lll11111ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llllllll11_opy_(instance: bstack111111l111_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack111111l111_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll11ll1_opy_(instance: bstack111111l111_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll111llll_opy_.logger.debug(bstack1l_opy_ (u"ࠦࡸ࡫ࡴࡠࡵࡷࡥࡹ࡫࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦ࡫ࡦࡻࡀࡿࡰ࡫ࡹࡾࠢࡹࡥࡱࡻࡥ࠾ࠤᔙ") + str(value) + bstack1l_opy_ (u"ࠧࠨᔚ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll111llll_opy_.bstack1ll11ll1ll1_opy_(target, strict)
        return bstack1lll111llll_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll111llll_opy_.bstack1ll11ll1ll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack1l11111l11l_opy_(self):
        return self.framework_name == bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᔛ")
    def bstack1l111111lll_opy_(self, target):
        return target if not self.bstack1l11111l11l_opy_() else self.bstack1l11111llll_opy_()
    @staticmethod
    def bstack1l11111llll_opy_():
        return str(os.getpid()) + str(threading.get_ident())