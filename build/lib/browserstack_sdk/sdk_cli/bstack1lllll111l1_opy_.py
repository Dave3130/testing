# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1ll1lll11ll_opy_ import bstack1ll1ll1111l_opy_, bstack1llll1111l1_opy_
import os
import threading
class bstack1lllll11ll1_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l1111_opy_ (u"ࠨࡈࡰࡱ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᕅ").format(self.name)
class bstack1lllllll1ll_opy_(Enum):
    NONE = 0
    bstack1llll11ll11_opy_ = 1
    bstack1ll1ll11l1l_opy_ = 3
    bstack1llll1l1l1l_opy_ = 4
    bstack11lllll1111_opy_ = 5
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
        return bstack11l1111_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᕆ").format(self.name)
class bstack1llll1ll11l_opy_(bstack1ll1ll1111l_opy_):
    framework_name: str
    framework_version: str
    state: bstack1lllllll1ll_opy_
    previous_state: bstack1lllllll1ll_opy_
    bstack1ll1lll1lll_opy_: datetime
    bstack11lllllllll_opy_: datetime
    def __init__(
        self,
        context: bstack1llll1111l1_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1lllllll1ll_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1lllllll1ll_opy_.NONE
        self.bstack1ll1lll1lll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack11lllllllll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llllll1111_opy_(self, bstack1l1111111ll_opy_: bstack1lllllll1ll_opy_):
        bstack1l111111111_opy_ = bstack1lllllll1ll_opy_(bstack1l1111111ll_opy_).name
        if not bstack1l111111111_opy_:
            return False
        if bstack1l1111111ll_opy_ == self.state:
            return False
        if self.state == bstack1lllllll1ll_opy_.bstack1ll1ll11l1l_opy_: # bstack11lllll1ll1_opy_ bstack11lllll1lll_opy_ for bstack11llll1llll_opy_ in Playwright, it bstack11llllll11l_opy_ bstack11lllll11l1_opy_ multiple times bstack11lllll1l11_opy_ a new state
            return True
        if (
            bstack1l1111111ll_opy_ == bstack1lllllll1ll_opy_.NONE
            or (self.state != bstack1lllllll1ll_opy_.NONE and bstack1l1111111ll_opy_ == bstack1lllllll1ll_opy_.bstack1llll11ll11_opy_)
            or (self.state < bstack1lllllll1ll_opy_.bstack1llll11ll11_opy_ and bstack1l1111111ll_opy_ == bstack1lllllll1ll_opy_.bstack1llll1l1l1l_opy_)
            or (self.state < bstack1lllllll1ll_opy_.bstack1llll11ll11_opy_ and bstack1l1111111ll_opy_ == bstack1lllllll1ll_opy_.QUIT)
        ):
            raise ValueError(bstack11l1111_opy_ (u"ࠣ࡫ࡱࡺࡦࡲࡩࡥࠢࡶࡸࡦࡺࡥࠡࡶࡵࡥࡳࡹࡩࡵ࡫ࡲࡲ࠿ࠦࠢᕇ") + str(self.state) + bstack11l1111_opy_ (u"ࠤࠣࡁࡃࠦࠢᕈ") + str(bstack1l1111111ll_opy_))
        self.previous_state = self.state
        self.state = bstack1l1111111ll_opy_
        self.bstack11lllllllll_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll111l11l_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1l1llll_opy_: Dict[str, bstack1llll1ll11l_opy_] = dict()
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
    def bstack1l1ll1l1l1l_opy_(self, instance: bstack1llll1ll11l_opy_, method_name: str, bstack1l1lll11111_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1ll1lll1l_opy_(
        self, method_name, previous_state: bstack1lllllll1ll_opy_, *args, **kwargs
    ) -> bstack1lllllll1ll_opy_:
        return
    @abc.abstractmethod
    def bstack1l1ll1l11ll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1ll1l1l11_opy_(self, bstack11lllll1l1l_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack11lllll1l1l_opy_:
                bstack11lllll111l_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack11lllll111l_opy_):
                    self.logger.warning(bstack11l1111_opy_ (u"ࠥࡹࡳࡶࡡࡵࡥ࡫ࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࠣᕉ") + str(method_name) + bstack11l1111_opy_ (u"ࠦࠧᕊ"))
                    continue
                bstack1l1ll1l1111_opy_ = self.bstack1l1ll1lll1l_opy_(
                    method_name, previous_state=bstack1lllllll1ll_opy_.NONE
                )
                bstack11llllll1ll_opy_ = self.bstack11lllllll1l_opy_(
                    method_name,
                    (bstack1l1ll1l1111_opy_ if bstack1l1ll1l1111_opy_ else bstack1lllllll1ll_opy_.NONE),
                    bstack11lllll111l_opy_,
                )
                if not callable(bstack11llllll1ll_opy_):
                    self.logger.warning(bstack11l1111_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠥࡴ࡯ࡵࠢࡳࡥࡹࡩࡨࡦࡦ࠽ࠤࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࠭ࢁࡳࡦ࡮ࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࡀࠠࠣᕋ") + str(self.framework_version) + bstack11l1111_opy_ (u"ࠨࠩࠣᕌ"))
                    continue
                setattr(clazz, method_name, bstack11llllll1ll_opy_)
    def bstack11lllllll1l_opy_(
        self,
        method_name: str,
        bstack1l1ll1l1111_opy_: bstack1lllllll1ll_opy_,
        bstack11lllll111l_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack11ll111l1_opy_ = datetime.now()
            (bstack1l1ll1l1111_opy_,) = wrapped.__vars__
            bstack1l1ll1l1111_opy_ = (
                bstack1l1ll1l1111_opy_
                if bstack1l1ll1l1111_opy_ and bstack1l1ll1l1111_opy_ != bstack1lllllll1ll_opy_.NONE
                else self.bstack1l1ll1lll1l_opy_(method_name, previous_state=bstack1l1ll1l1111_opy_, *args, **kwargs)
            )
            if bstack1l1ll1l1111_opy_ == bstack1lllllll1ll_opy_.bstack1llll11ll11_opy_:
                ctx = bstack1ll1ll1111l_opy_.create_context(self.bstack11llllll1l1_opy_(target))
                if not self.bstack11llllll111_opy_() or ctx.id not in bstack1lll111l11l_opy_.bstack1lll1l1llll_opy_:
                    bstack1lll111l11l_opy_.bstack1lll1l1llll_opy_[ctx.id] = bstack1llll1ll11l_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1ll1l1111_opy_
                    )
                self.logger.debug(bstack11l1111_opy_ (u"ࠢࡸࡴࡤࡴࡵ࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤࠡࡥࡵࡩࡦࡺࡥࡥ࠼ࠣࡿࡹࡧࡲࡨࡧࡷ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡩࡴࡹ࠿ࡾࡧࡹࡾ࠮ࡪࡦࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡹ࠽ࠣᕍ") + str(bstack1lll111l11l_opy_.bstack1lll1l1llll_opy_.keys()) + bstack11l1111_opy_ (u"ࠣࠤᕎ"))
            else:
                self.logger.debug(bstack11l1111_opy_ (u"ࠤࡺࡶࡦࡶࡰࡦࡦࠣࡱࡪࡺࡨࡰࡦࠣ࡭ࡳࡼ࡯࡬ࡧࡧ࠾ࠥࢁࡴࡢࡴࡪࡩࡹ࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦᕏ") + str(bstack1lll111l11l_opy_.bstack1lll1l1llll_opy_.keys()) + bstack11l1111_opy_ (u"ࠥࠦᕐ"))
            instance = bstack1lll111l11l_opy_.bstack1l1lll1l1ll_opy_(self.bstack11llllll1l1_opy_(target))
            if bstack1l1ll1l1111_opy_ == bstack1lllllll1ll_opy_.NONE or not instance:
                ctx = bstack1ll1ll1111l_opy_.create_context(self.bstack11llllll1l1_opy_(target))
                self.logger.warning(bstack11l1111_opy_ (u"ࠦࡼࡸࡡࡱࡲࡨࡨࠥࡳࡥࡵࡪࡲࡨࠥࡻ࡮ࡵࡴࡤࡧࡰ࡫ࡤ࠻ࠢࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡥࡷࡼࡂࢁࡣࡵࡺࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡹ࠽ࠣᕑ") + str(bstack1lll111l11l_opy_.bstack1lll1l1llll_opy_.keys()) + bstack11l1111_opy_ (u"ࠧࠨᕒ"))
                return bstack11lllll111l_opy_(target, *args, **kwargs)
            bstack1l1ll1111l1_opy_ = self.bstack1l1ll1l11ll_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1l1111_opy_, bstack1lllll11ll1_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1llllll1111_opy_(bstack1l1ll1l1111_opy_):
                self.logger.debug(bstack11l1111_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡪࡪࠠࡴࡶࡤࡸࡪ࠳ࡴࡳࡣࡱࡷ࡮ࡺࡩࡰࡰ࠽ࠤࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡱࡴࡨࡺ࡮ࡵࡵࡴࡡࡶࡸࡦࡺࡥࡾࠢࡀࡂࠥࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡵࡷࡥࡹ࡫ࡽࠡࠪࡾࡸࡾࡶࡥࠩࡶࡤࡶ࡬࡫ࡴࠪࡿ࠱ࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡿࡦࡸࡧࡴࡿࠬࠤࡠࠨᕓ") + str(instance.ref()) + bstack11l1111_opy_ (u"ࠢ࡞ࠤᕔ"))
            result = (
                bstack1l1ll1111l1_opy_(target, bstack11lllll111l_opy_, *args, **kwargs)
                if callable(bstack1l1ll1111l1_opy_)
                else bstack11lllll111l_opy_(target, *args, **kwargs)
            )
            bstack11lllllll11_opy_ = self.bstack1l1ll1l11ll_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1l1111_opy_, bstack1lllll11ll1_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1ll1l1l1l_opy_(instance, method_name, datetime.now() - bstack11ll111l1_opy_, *args, **kwargs)
            return bstack11lllllll11_opy_ if bstack11lllllll11_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1ll1l1111_opy_,)
        return wrapped
    @staticmethod
    def bstack1l1lll1l1ll_opy_(target: object, strict=True):
        ctx = bstack1ll1ll1111l_opy_.create_context(target)
        instance = bstack1lll111l11l_opy_.bstack1lll1l1llll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll11111_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1ll1l1_opy_(
        ctx: bstack1llll1111l1_opy_, state: bstack1lllllll1ll_opy_, reverse=True
    ) -> List[bstack1llll1ll11l_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll111l11l_opy_.bstack1lll1l1llll_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lll1lll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllllll1l1_opy_(instance: bstack1llll1ll11l_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llll1ll11l_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llllll1111_opy_(instance: bstack1llll1ll11l_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll111l11l_opy_.logger.debug(bstack11l1111_opy_ (u"ࠣࡵࡨࡸࡤࡹࡴࡢࡶࡨ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣ࡯ࡪࡿ࠽ࡼ࡭ࡨࡽࢂࠦࡶࡢ࡮ࡸࡩࡂࠨᕕ") + str(value) + bstack11l1111_opy_ (u"ࠤࠥᕖ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll111l11l_opy_.bstack1l1lll1l1ll_opy_(target, strict)
        return bstack1lll111l11l_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll111l11l_opy_.bstack1l1lll1l1ll_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack11llllll111_opy_(self):
        return self.framework_name == bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᕗ")
    def bstack11llllll1l1_opy_(self, target):
        return target if not self.bstack11llllll111_opy_() else self.bstack11lllll11ll_opy_()
    @staticmethod
    def bstack11lllll11ll_opy_():
        return str(os.getpid()) + str(threading.get_ident())