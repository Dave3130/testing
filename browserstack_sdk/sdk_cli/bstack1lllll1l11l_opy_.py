# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1ll11111_opy_, bstack1lll1l1l1ll_opy_
import os
import threading
class bstack1llllll11ll_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l11ll_opy_ (u"ࠧࡎ࡯ࡰ࡭ࡖࡸࡦࡺࡥ࠯ࡽࢀࠦᔶ").format(self.name)
class bstack1lllll1l1ll_opy_(Enum):
    NONE = 0
    bstack1llllll1lll_opy_ = 1
    bstack1ll1ll1l111_opy_ = 3
    bstack1lllll1ll1l_opy_ = 4
    bstack11lllllll1l_opy_ = 5
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
        return bstack11l11ll_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᔷ").format(self.name)
class bstack1llll1llll1_opy_(bstack1ll1ll11111_opy_):
    framework_name: str
    framework_version: str
    state: bstack1lllll1l1ll_opy_
    previous_state: bstack1lllll1l1ll_opy_
    bstack1ll1lll1l11_opy_: datetime
    bstack1l1111111ll_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1l1l1ll_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1lllll1l1ll_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1lllll1l1ll_opy_.NONE
        self.bstack1ll1lll1l11_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111111ll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll1l1l11_opy_(self, bstack1l11111l111_opy_: bstack1lllll1l1ll_opy_):
        bstack1l111111l11_opy_ = bstack1lllll1l1ll_opy_(bstack1l11111l111_opy_).name
        if not bstack1l111111l11_opy_:
            return False
        if bstack1l11111l111_opy_ == self.state:
            return False
        if self.state == bstack1lllll1l1ll_opy_.bstack1ll1ll1l111_opy_: # bstack11llllll111_opy_ bstack1l11111111l_opy_ for bstack11lllll1l11_opy_ in Playwright, it bstack1l1111111l1_opy_ bstack11llllll11l_opy_ multiple times bstack11lllll1l1l_opy_ a new state
            return True
        if (
            bstack1l11111l111_opy_ == bstack1lllll1l1ll_opy_.NONE
            or (self.state != bstack1lllll1l1ll_opy_.NONE and bstack1l11111l111_opy_ == bstack1lllll1l1ll_opy_.bstack1llllll1lll_opy_)
            or (self.state < bstack1lllll1l1ll_opy_.bstack1llllll1lll_opy_ and bstack1l11111l111_opy_ == bstack1lllll1l1ll_opy_.bstack1lllll1ll1l_opy_)
            or (self.state < bstack1lllll1l1ll_opy_.bstack1llllll1lll_opy_ and bstack1l11111l111_opy_ == bstack1lllll1l1ll_opy_.QUIT)
        ):
            raise ValueError(bstack11l11ll_opy_ (u"ࠢࡪࡰࡹࡥࡱ࡯ࡤࠡࡵࡷࡥࡹ࡫ࠠࡵࡴࡤࡲࡸ࡯ࡴࡪࡱࡱ࠾ࠥࠨᔸ") + str(self.state) + bstack11l11ll_opy_ (u"ࠣࠢࡀࡂࠥࠨᔹ") + str(bstack1l11111l111_opy_))
        self.previous_state = self.state
        self.state = bstack1l11111l111_opy_
        self.bstack1l1111111ll_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1ll1llllll1_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll11l11ll_opy_: Dict[str, bstack1llll1llll1_opy_] = dict()
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
    def bstack1l1ll1llll1_opy_(self, instance: bstack1llll1llll1_opy_, method_name: str, bstack1l1ll1l11l1_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1ll1lll11_opy_(
        self, method_name, previous_state: bstack1lllll1l1ll_opy_, *args, **kwargs
    ) -> bstack1lllll1l1ll_opy_:
        return
    @abc.abstractmethod
    def bstack1l1lll1111l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1ll1l11ll_opy_(self, bstack11lllll1ll1_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack11lllll1ll1_opy_:
                bstack11llllll1ll_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack11llllll1ll_opy_):
                    self.logger.warning(bstack11l11ll_opy_ (u"ࠤࡸࡲࡵࡧࡴࡤࡪࡨࡨࠥࡳࡥࡵࡪࡲࡨ࠿ࠦࠢᔺ") + str(method_name) + bstack11l11ll_opy_ (u"ࠥࠦᔻ"))
                    continue
                bstack1l1ll1ll111_opy_ = self.bstack1l1ll1lll11_opy_(
                    method_name, previous_state=bstack1lllll1l1ll_opy_.NONE
                )
                bstack11llllll1l1_opy_ = self.bstack11lllllll11_opy_(
                    method_name,
                    (bstack1l1ll1ll111_opy_ if bstack1l1ll1ll111_opy_ else bstack1lllll1l1ll_opy_.NONE),
                    bstack11llllll1ll_opy_,
                )
                if not callable(bstack11llllll1l1_opy_):
                    self.logger.warning(bstack11l11ll_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠤࡳࡵࡴࠡࡲࡤࡸࡨ࡮ࡥࡥ࠼ࠣࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࠬࢀࡹࡥ࡭ࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁ࠿ࠦࠢᔼ") + str(self.framework_version) + bstack11l11ll_opy_ (u"ࠧ࠯ࠢᔽ"))
                    continue
                setattr(clazz, method_name, bstack11llllll1l1_opy_)
    def bstack11lllllll11_opy_(
        self,
        method_name: str,
        bstack1l1ll1ll111_opy_: bstack1lllll1l1ll_opy_,
        bstack11llllll1ll_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1lll1l1l11_opy_ = datetime.now()
            (bstack1l1ll1ll111_opy_,) = wrapped.__vars__
            bstack1l1ll1ll111_opy_ = (
                bstack1l1ll1ll111_opy_
                if bstack1l1ll1ll111_opy_ and bstack1l1ll1ll111_opy_ != bstack1lllll1l1ll_opy_.NONE
                else self.bstack1l1ll1lll11_opy_(method_name, previous_state=bstack1l1ll1ll111_opy_, *args, **kwargs)
            )
            if bstack1l1ll1ll111_opy_ == bstack1lllll1l1ll_opy_.bstack1llllll1lll_opy_:
                ctx = bstack1ll1ll11111_opy_.create_context(self.bstack11llllllll1_opy_(target))
                if not self.bstack1l111111111_opy_() or ctx.id not in bstack1ll1llllll1_opy_.bstack1lll11l11ll_opy_:
                    bstack1ll1llllll1_opy_.bstack1lll11l11ll_opy_[ctx.id] = bstack1llll1llll1_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1ll1ll111_opy_
                    )
                self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡷࡳࡣࡳࡴࡪࡪࠠ࡮ࡧࡷ࡬ࡴࡪࠠࡤࡴࡨࡥࡹ࡫ࡤ࠻ࠢࡾࡸࡦࡸࡧࡦࡶ࠱ࡣࡤࡩ࡬ࡢࡵࡶࡣࡤࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡨࡺࡸ࠾ࡽࡦࡸࡽ࠴ࡩࡥࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡸࡃࠢᔾ") + str(bstack1ll1llllll1_opy_.bstack1lll11l11ll_opy_.keys()) + bstack11l11ll_opy_ (u"ࠢࠣᔿ"))
            else:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡹࡵࡥࡵࡶࡥࡥࠢࡰࡩࡹ࡮࡯ࡥࠢ࡬ࡲࡻࡵ࡫ࡦࡦ࠽ࠤࢀࡺࡡࡳࡩࡨࡸ࠳ࡥ࡟ࡤ࡮ࡤࡷࡸࡥ࡟ࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥᕀ") + str(bstack1ll1llllll1_opy_.bstack1lll11l11ll_opy_.keys()) + bstack11l11ll_opy_ (u"ࠤࠥᕁ"))
            instance = bstack1ll1llllll1_opy_.bstack1ll11l11ll1_opy_(self.bstack11llllllll1_opy_(target))
            if bstack1l1ll1ll111_opy_ == bstack1lllll1l1ll_opy_.NONE or not instance:
                ctx = bstack1ll1ll11111_opy_.create_context(self.bstack11llllllll1_opy_(target))
                self.logger.warning(bstack11l11ll_opy_ (u"ࠥࡻࡷࡧࡰࡱࡧࡧࠤࡲ࡫ࡴࡩࡱࡧࠤࡺࡴࡴࡳࡣࡦ࡯ࡪࡪ࠺ࠡࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡤࡶࡻࡁࢀࡩࡴࡹࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡸࡃࠢᕂ") + str(bstack1ll1llllll1_opy_.bstack1lll11l11ll_opy_.keys()) + bstack11l11ll_opy_ (u"ࠦࠧᕃ"))
                return bstack11llllll1ll_opy_(target, *args, **kwargs)
            bstack1l1ll111ll1_opy_ = self.bstack1l1lll1111l_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1ll111_opy_, bstack1llllll11ll_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1llll1l1l11_opy_(bstack1l1ll1ll111_opy_):
                self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡧࡰࡱ࡮࡬ࡩࡩࠦࡳࡵࡣࡷࡩ࠲ࡺࡲࡢࡰࡶ࡭ࡹ࡯࡯࡯࠼ࠣࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡰࡳࡧࡹ࡭ࡴࡻࡳࡠࡵࡷࡥࡹ࡫ࡽࠡ࠿ࡁࠤࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡴࡶࡤࡸࡪࢃࠠࠩࡽࡷࡽࡵ࡫ࠨࡵࡣࡵ࡫ࡪࡺࠩࡾ࠰ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡾࡥࡷ࡭ࡳࡾࠫࠣ࡟ࠧᕄ") + str(instance.ref()) + bstack11l11ll_opy_ (u"ࠨ࡝ࠣᕅ"))
            result = (
                bstack1l1ll111ll1_opy_(target, bstack11llllll1ll_opy_, *args, **kwargs)
                if callable(bstack1l1ll111ll1_opy_)
                else bstack11llllll1ll_opy_(target, *args, **kwargs)
            )
            bstack11lllll1lll_opy_ = self.bstack1l1lll1111l_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1ll111_opy_, bstack1llllll11ll_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1ll1llll1_opy_(instance, method_name, datetime.now() - bstack1lll1l1l11_opy_, *args, **kwargs)
            return bstack11lllll1lll_opy_ if bstack11lllll1lll_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1ll1ll111_opy_,)
        return wrapped
    @staticmethod
    def bstack1ll11l11ll1_opy_(target: object, strict=True):
        ctx = bstack1ll1ll11111_opy_.create_context(target)
        instance = bstack1ll1llllll1_opy_.bstack1lll11l11ll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll111l1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1l1111_opy_(
        ctx: bstack1lll1l1l1ll_opy_, state: bstack1lllll1l1ll_opy_, reverse=True
    ) -> List[bstack1llll1llll1_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1ll1llllll1_opy_.bstack1lll11l11ll_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lll1l11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llllll11l1_opy_(instance: bstack1llll1llll1_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llll1llll1_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll1l1l11_opy_(instance: bstack1llll1llll1_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1ll1llllll1_opy_.logger.debug(bstack11l11ll_opy_ (u"ࠢࡴࡧࡷࡣࡸࡺࡡࡵࡧ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢ࡮ࡩࡾࡃࡻ࡬ࡧࡼࢁࠥࡼࡡ࡭ࡷࡨࡁࠧᕆ") + str(value) + bstack11l11ll_opy_ (u"ࠣࠤᕇ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1ll1llllll1_opy_.bstack1ll11l11ll1_opy_(target, strict)
        return bstack1ll1llllll1_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1ll1llllll1_opy_.bstack1ll11l11ll1_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack1l111111111_opy_(self):
        return self.framework_name == bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᕈ")
    def bstack11llllllll1_opy_(self, target):
        return target if not self.bstack1l111111111_opy_() else self.bstack11lllllllll_opy_()
    @staticmethod
    def bstack11lllllllll_opy_():
        return str(os.getpid()) + str(threading.get_ident())