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
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1ll1lll11l1_opy_ import bstack1ll1ll11111_opy_, bstack1lll1lll1ll_opy_
import os
import threading
class bstack1llll11llll_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11ll1ll_opy_ (u"ࠢࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᕆ").format(self.name)
class bstack1llll1l1ll1_opy_(Enum):
    NONE = 0
    bstack1llllllll1l_opy_ = 1
    bstack1ll1ll11lll_opy_ = 3
    bstack1llll1lll11_opy_ = 4
    bstack11lllll1ll1_opy_ = 5
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
        return bstack11ll1ll_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡣࡷࡩ࠳ࢁࡽࠣᕇ").format(self.name)
class bstack1llll111l1l_opy_(bstack1ll1ll11111_opy_):
    framework_name: str
    framework_version: str
    state: bstack1llll1l1ll1_opy_
    previous_state: bstack1llll1l1ll1_opy_
    bstack1ll1llll1l1_opy_: datetime
    bstack1l1111111l1_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1lll1ll_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1llll1l1ll1_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1llll1l1ll1_opy_.NONE
        self.bstack1ll1llll1l1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111111l1_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllllll1l1_opy_(self, bstack11llllllll1_opy_: bstack1llll1l1ll1_opy_):
        bstack1l1111111ll_opy_ = bstack1llll1l1ll1_opy_(bstack11llllllll1_opy_).name
        if not bstack1l1111111ll_opy_:
            return False
        if bstack11llllllll1_opy_ == self.state:
            return False
        if self.state == bstack1llll1l1ll1_opy_.bstack1ll1ll11lll_opy_: # bstack11lllll111l_opy_ bstack11llll1llll_opy_ for bstack11lllllll11_opy_ in Playwright, it bstack11lllll1111_opy_ bstack11lllll11l1_opy_ multiple times bstack11lllll1lll_opy_ a new state
            return True
        if (
            bstack11llllllll1_opy_ == bstack1llll1l1ll1_opy_.NONE
            or (self.state != bstack1llll1l1ll1_opy_.NONE and bstack11llllllll1_opy_ == bstack1llll1l1ll1_opy_.bstack1llllllll1l_opy_)
            or (self.state < bstack1llll1l1ll1_opy_.bstack1llllllll1l_opy_ and bstack11llllllll1_opy_ == bstack1llll1l1ll1_opy_.bstack1llll1lll11_opy_)
            or (self.state < bstack1llll1l1ll1_opy_.bstack1llllllll1l_opy_ and bstack11llllllll1_opy_ == bstack1llll1l1ll1_opy_.QUIT)
        ):
            raise ValueError(bstack11ll1ll_opy_ (u"ࠤ࡬ࡲࡻࡧ࡬ࡪࡦࠣࡷࡹࡧࡴࡦࠢࡷࡶࡦࡴࡳࡪࡶ࡬ࡳࡳࡀࠠࠣᕈ") + str(self.state) + bstack11ll1ll_opy_ (u"ࠥࠤࡂࡄࠠࠣᕉ") + str(bstack11llllllll1_opy_))
        self.previous_state = self.state
        self.state = bstack11llllllll1_opy_
        self.bstack1l1111111l1_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll1111l11_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llll111111_opy_: Dict[str, bstack1llll111l1l_opy_] = dict()
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
    def bstack1l1ll1ll1l1_opy_(self, instance: bstack1llll111l1l_opy_, method_name: str, bstack1l1lll11111_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1ll1l1l11_opy_(
        self, method_name, previous_state: bstack1llll1l1ll1_opy_, *args, **kwargs
    ) -> bstack1llll1l1ll1_opy_:
        return
    @abc.abstractmethod
    def bstack1l1lll111l1_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1lll1111l_opy_(self, bstack11lllll1l11_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack11lllll1l11_opy_:
                bstack11llllll1ll_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack11llllll1ll_opy_):
                    self.logger.warning(bstack11ll1ll_opy_ (u"ࠦࡺࡴࡰࡢࡶࡦ࡬ࡪࡪࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࠤᕊ") + str(method_name) + bstack11ll1ll_opy_ (u"ࠧࠨᕋ"))
                    continue
                bstack1l1ll1l11l1_opy_ = self.bstack1l1ll1l1l11_opy_(
                    method_name, previous_state=bstack1llll1l1ll1_opy_.NONE
                )
                bstack11llllll1l1_opy_ = self.bstack11llllll111_opy_(
                    method_name,
                    (bstack1l1ll1l11l1_opy_ if bstack1l1ll1l11l1_opy_ else bstack1llll1l1ll1_opy_.NONE),
                    bstack11llllll1ll_opy_,
                )
                if not callable(bstack11llllll1l1_opy_):
                    self.logger.warning(bstack11ll1ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠦ࡮ࡰࡶࠣࡴࡦࡺࡣࡩࡧࡧ࠾ࠥࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࠮ࡻࡴࡧ࡯ࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃ࠺ࠡࠤᕌ") + str(self.framework_version) + bstack11ll1ll_opy_ (u"ࠢࠪࠤᕍ"))
                    continue
                setattr(clazz, method_name, bstack11llllll1l1_opy_)
    def bstack11llllll111_opy_(
        self,
        method_name: str,
        bstack1l1ll1l11l1_opy_: bstack1llll1l1ll1_opy_,
        bstack11llllll1ll_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack111111ll11_opy_ = datetime.now()
            (bstack1l1ll1l11l1_opy_,) = wrapped.__vars__
            bstack1l1ll1l11l1_opy_ = (
                bstack1l1ll1l11l1_opy_
                if bstack1l1ll1l11l1_opy_ and bstack1l1ll1l11l1_opy_ != bstack1llll1l1ll1_opy_.NONE
                else self.bstack1l1ll1l1l11_opy_(method_name, previous_state=bstack1l1ll1l11l1_opy_, *args, **kwargs)
            )
            if bstack1l1ll1l11l1_opy_ == bstack1llll1l1ll1_opy_.bstack1llllllll1l_opy_:
                ctx = bstack1ll1ll11111_opy_.create_context(self.bstack11lllllll1l_opy_(target))
                if not self.bstack11lllll11ll_opy_() or ctx.id not in bstack1lll1111l11_opy_.bstack1llll111111_opy_:
                    bstack1lll1111l11_opy_.bstack1llll111111_opy_[ctx.id] = bstack1llll111l1l_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1ll1l11l1_opy_
                    )
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠣࡹࡵࡥࡵࡶࡥࡥࠢࡰࡩࡹ࡮࡯ࡥࠢࡦࡶࡪࡧࡴࡦࡦ࠽ࠤࢀࡺࡡࡳࡩࡨࡸ࠳ࡥ࡟ࡤ࡮ࡤࡷࡸࡥ࡟ࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡣࡵࡺࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᕎ") + str(bstack1lll1111l11_opy_.bstack1llll111111_opy_.keys()) + bstack11ll1ll_opy_ (u"ࠤࠥᕏ"))
            else:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡻࡷࡧࡰࡱࡧࡧࠤࡲ࡫ࡴࡩࡱࡧࠤ࡮ࡴࡶࡰ࡭ࡨࡨ࠿ࠦࡻࡵࡣࡵ࡫ࡪࡺ࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧᕐ") + str(bstack1lll1111l11_opy_.bstack1llll111111_opy_.keys()) + bstack11ll1ll_opy_ (u"ࠦࠧᕑ"))
            instance = bstack1lll1111l11_opy_.bstack1ll11l1ll11_opy_(self.bstack11lllllll1l_opy_(target))
            if bstack1l1ll1l11l1_opy_ == bstack1llll1l1ll1_opy_.NONE or not instance:
                ctx = bstack1ll1ll11111_opy_.create_context(self.bstack11lllllll1l_opy_(target))
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡵ࡯ࡶࡵࡥࡨࡱࡥࡥ࠼ࠣࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡦࡸࡽࡃࡻࡤࡶࡻࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᕒ") + str(bstack1lll1111l11_opy_.bstack1llll111111_opy_.keys()) + bstack11ll1ll_opy_ (u"ࠨࠢᕓ"))
                return bstack11llllll1ll_opy_(target, *args, **kwargs)
            bstack1l1ll1111ll_opy_ = self.bstack1l1lll111l1_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1l11l1_opy_, bstack1llll11llll_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1lllllll1l1_opy_(bstack1l1ll1l11l1_opy_):
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡢࡲࡳࡰ࡮࡫ࡤࠡࡵࡷࡥࡹ࡫࠭ࡵࡴࡤࡲࡸ࡯ࡴࡪࡱࡱ࠾ࠥࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡲࡵࡩࡻ࡯࡯ࡶࡵࡢࡷࡹࡧࡴࡦࡿࠣࡁࡃࠦࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡶࡸࡦࡺࡥࡾࠢࠫࡿࡹࡿࡰࡦࠪࡷࡥࡷ࡭ࡥࡵࠫࢀ࠲ࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤࢀࡧࡲࡨࡵࢀ࠭ࠥࡡࠢᕔ") + str(instance.ref()) + bstack11ll1ll_opy_ (u"ࠣ࡟ࠥᕕ"))
            result = (
                bstack1l1ll1111ll_opy_(target, bstack11llllll1ll_opy_, *args, **kwargs)
                if callable(bstack1l1ll1111ll_opy_)
                else bstack11llllll1ll_opy_(target, *args, **kwargs)
            )
            bstack11lllll1l1l_opy_ = self.bstack1l1lll111l1_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1l11l1_opy_, bstack1llll11llll_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1ll1ll1l1_opy_(instance, method_name, datetime.now() - bstack111111ll11_opy_, *args, **kwargs)
            return bstack11lllll1l1l_opy_ if bstack11lllll1l1l_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1ll1l11l1_opy_,)
        return wrapped
    @staticmethod
    def bstack1ll11l1ll11_opy_(target: object, strict=True):
        ctx = bstack1ll1ll11111_opy_.create_context(target)
        instance = bstack1lll1111l11_opy_.bstack1llll111111_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1l1lllll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l11l1ll_opy_(
        ctx: bstack1lll1lll1ll_opy_, state: bstack1llll1l1ll1_opy_, reverse=True
    ) -> List[bstack1llll111l1l_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll1111l11_opy_.bstack1llll111111_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1llll1l1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllll1llll_opy_(instance: bstack1llll111l1l_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llll111l1l_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllllll1l1_opy_(instance: bstack1llll111l1l_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll1111l11_opy_.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡰ࡫ࡹ࠾ࡽ࡮ࡩࡾࢃࠠࡷࡣ࡯ࡹࡪࡃࠢᕖ") + str(value) + bstack11ll1ll_opy_ (u"ࠥࠦᕗ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll1111l11_opy_.bstack1ll11l1ll11_opy_(target, strict)
        return bstack1lll1111l11_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll1111l11_opy_.bstack1ll11l1ll11_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack11lllll11ll_opy_(self):
        return self.framework_name == bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᕘ")
    def bstack11lllllll1l_opy_(self, target):
        return target if not self.bstack11lllll11ll_opy_() else self.bstack11llllll11l_opy_()
    @staticmethod
    def bstack11llllll11l_opy_():
        return str(os.getpid()) + str(threading.get_ident())