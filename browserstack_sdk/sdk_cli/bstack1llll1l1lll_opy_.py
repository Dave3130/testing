# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1ll1lll11l1_opy_, bstack1llll11l1l1_opy_
import os
import threading
class bstack1lllll1lll1_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1lllll1_opy_ (u"ࠢࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨᔇ").format(self.name)
class bstack1llll1ll1ll_opy_(Enum):
    NONE = 0
    bstack1llll1ll111_opy_ = 1
    bstack1ll1llll1ll_opy_ = 3
    bstack1lllll1l1l1_opy_ = 4
    bstack1l11111llll_opy_ = 5
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
        return bstack1lllll1_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡣࡷࡩ࠳ࢁࡽࠣᔈ").format(self.name)
class bstack1111111l11_opy_(bstack1ll1lll11l1_opy_):
    framework_name: str
    framework_version: str
    state: bstack1llll1ll1ll_opy_
    previous_state: bstack1llll1ll1ll_opy_
    bstack1lll111l111_opy_: datetime
    bstack1l1111l1lll_opy_: datetime
    def __init__(
        self,
        context: bstack1llll11l1l1_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1llll1ll1ll_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1llll1ll1ll_opy_.NONE
        self.bstack1lll111l111_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l1lll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll1l11l_opy_(self, bstack1l1111l1l1l_opy_: bstack1llll1ll1ll_opy_):
        bstack1l1111l11l1_opy_ = bstack1llll1ll1ll_opy_(bstack1l1111l1l1l_opy_).name
        if not bstack1l1111l11l1_opy_:
            return False
        if bstack1l1111l1l1l_opy_ == self.state:
            return False
        if self.state == bstack1llll1ll1ll_opy_.bstack1ll1llll1ll_opy_: # bstack1l11111lll1_opy_ bstack1l1111l1111_opy_ for bstack1l11111ll11_opy_ in Playwright, it bstack1l11111l11l_opy_ bstack1l1111l111l_opy_ multiple times bstack1l111111lll_opy_ a new state
            return True
        if (
            bstack1l1111l1l1l_opy_ == bstack1llll1ll1ll_opy_.NONE
            or (self.state != bstack1llll1ll1ll_opy_.NONE and bstack1l1111l1l1l_opy_ == bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_)
            or (self.state < bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_ and bstack1l1111l1l1l_opy_ == bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_)
            or (self.state < bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_ and bstack1l1111l1l1l_opy_ == bstack1llll1ll1ll_opy_.QUIT)
        ):
            raise ValueError(bstack1lllll1_opy_ (u"ࠤ࡬ࡲࡻࡧ࡬ࡪࡦࠣࡷࡹࡧࡴࡦࠢࡷࡶࡦࡴࡳࡪࡶ࡬ࡳࡳࡀࠠࠣᔉ") + str(self.state) + bstack1lllll1_opy_ (u"ࠥࠤࡂࡄࠠࠣᔊ") + str(bstack1l1111l1l1l_opy_))
        self.previous_state = self.state
        self.state = bstack1l1111l1l1l_opy_
        self.bstack1l1111l1lll_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll11ll1l1_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1llll11_opy_: Dict[str, bstack1111111l11_opy_] = dict()
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
    def bstack1l1llll11ll_opy_(self, instance: bstack1111111l11_opy_, method_name: str, bstack1l1lll1l11l_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1llll11l1_opy_(
        self, method_name, previous_state: bstack1llll1ll1ll_opy_, *args, **kwargs
    ) -> bstack1llll1ll1ll_opy_:
        return
    @abc.abstractmethod
    def bstack1l1lll11l1l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1llll1ll1_opy_(self, bstack1l111111ll1_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack1l111111ll1_opy_:
                bstack1l11111l1l1_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1l11111l1l1_opy_):
                    self.logger.warning(bstack1lllll1_opy_ (u"ࠦࡺࡴࡰࡢࡶࡦ࡬ࡪࡪࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࠤᔋ") + str(method_name) + bstack1lllll1_opy_ (u"ࠧࠨᔌ"))
                    continue
                bstack1l1lll1ll1l_opy_ = self.bstack1l1llll11l1_opy_(
                    method_name, previous_state=bstack1llll1ll1ll_opy_.NONE
                )
                bstack1l111111l11_opy_ = self.bstack1l11111ll1l_opy_(
                    method_name,
                    (bstack1l1lll1ll1l_opy_ if bstack1l1lll1ll1l_opy_ else bstack1llll1ll1ll_opy_.NONE),
                    bstack1l11111l1l1_opy_,
                )
                if not callable(bstack1l111111l11_opy_):
                    self.logger.warning(bstack1lllll1_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠦ࡮ࡰࡶࠣࡴࡦࡺࡣࡩࡧࡧ࠾ࠥࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࠮ࡻࡴࡧ࡯ࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃ࠺ࠡࠤᔍ") + str(self.framework_version) + bstack1lllll1_opy_ (u"ࠢࠪࠤᔎ"))
                    continue
                setattr(clazz, method_name, bstack1l111111l11_opy_)
    def bstack1l11111ll1l_opy_(
        self,
        method_name: str,
        bstack1l1lll1ll1l_opy_: bstack1llll1ll1ll_opy_,
        bstack1l11111l1l1_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1l11llll11_opy_ = datetime.now()
            (bstack1l1lll1ll1l_opy_,) = wrapped.__vars__
            bstack1l1lll1ll1l_opy_ = (
                bstack1l1lll1ll1l_opy_
                if bstack1l1lll1ll1l_opy_ and bstack1l1lll1ll1l_opy_ != bstack1llll1ll1ll_opy_.NONE
                else self.bstack1l1llll11l1_opy_(method_name, previous_state=bstack1l1lll1ll1l_opy_, *args, **kwargs)
            )
            if bstack1l1lll1ll1l_opy_ == bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_:
                ctx = bstack1ll1lll11l1_opy_.create_context(self.bstack1l1111111ll_opy_(target))
                if not self.bstack1l11111l111_opy_() or ctx.id not in bstack1lll11ll1l1_opy_.bstack1lll1llll11_opy_:
                    bstack1lll11ll1l1_opy_.bstack1lll1llll11_opy_[ctx.id] = bstack1111111l11_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1lll1ll1l_opy_
                    )
                self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡹࡵࡥࡵࡶࡥࡥࠢࡰࡩࡹ࡮࡯ࡥࠢࡦࡶࡪࡧࡴࡦࡦ࠽ࠤࢀࡺࡡࡳࡩࡨࡸ࠳ࡥ࡟ࡤ࡮ࡤࡷࡸࡥ࡟ࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡣࡵࡺࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᔏ") + str(bstack1lll11ll1l1_opy_.bstack1lll1llll11_opy_.keys()) + bstack1lllll1_opy_ (u"ࠤࠥᔐ"))
            else:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡻࡷࡧࡰࡱࡧࡧࠤࡲ࡫ࡴࡩࡱࡧࠤ࡮ࡴࡶࡰ࡭ࡨࡨ࠿ࠦࡻࡵࡣࡵ࡫ࡪࡺ࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧᔑ") + str(bstack1lll11ll1l1_opy_.bstack1lll1llll11_opy_.keys()) + bstack1lllll1_opy_ (u"ࠦࠧᔒ"))
            instance = bstack1lll11ll1l1_opy_.bstack1ll11lll11l_opy_(self.bstack1l1111111ll_opy_(target))
            if bstack1l1lll1ll1l_opy_ == bstack1llll1ll1ll_opy_.NONE or not instance:
                ctx = bstack1ll1lll11l1_opy_.create_context(self.bstack1l1111111ll_opy_(target))
                self.logger.warning(bstack1lllll1_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡵ࡯ࡶࡵࡥࡨࡱࡥࡥ࠼ࠣࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡦࡸࡽࡃࡻࡤࡶࡻࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᔓ") + str(bstack1lll11ll1l1_opy_.bstack1lll1llll11_opy_.keys()) + bstack1lllll1_opy_ (u"ࠨࠢᔔ"))
                return bstack1l11111l1l1_opy_(target, *args, **kwargs)
            bstack1l1ll1l11l1_opy_ = self.bstack1l1lll11l1l_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll1ll1l_opy_, bstack1lllll1lll1_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1lllll1l11l_opy_(bstack1l1lll1ll1l_opy_):
                self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡢࡲࡳࡰ࡮࡫ࡤࠡࡵࡷࡥࡹ࡫࠭ࡵࡴࡤࡲࡸ࡯ࡴࡪࡱࡱ࠾ࠥࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡲࡵࡩࡻ࡯࡯ࡶࡵࡢࡷࡹࡧࡴࡦࡿࠣࡁࡃࠦࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡶࡸࡦࡺࡥࡾࠢࠫࡿࡹࡿࡰࡦࠪࡷࡥࡷ࡭ࡥࡵࠫࢀ࠲ࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤࢀࡧࡲࡨࡵࢀ࠭ࠥࡡࠢᔕ") + str(instance.ref()) + bstack1lllll1_opy_ (u"ࠣ࡟ࠥᔖ"))
            result = (
                bstack1l1ll1l11l1_opy_(target, bstack1l11111l1l1_opy_, *args, **kwargs)
                if callable(bstack1l1ll1l11l1_opy_)
                else bstack1l11111l1l1_opy_(target, *args, **kwargs)
            )
            bstack1l111111l1l_opy_ = self.bstack1l1lll11l1l_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll1ll1l_opy_, bstack1lllll1lll1_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1llll11ll_opy_(instance, method_name, datetime.now() - bstack1l11llll11_opy_, *args, **kwargs)
            return bstack1l111111l1l_opy_ if bstack1l111111l1l_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1lll1ll1l_opy_,)
        return wrapped
    @staticmethod
    def bstack1ll11lll11l_opy_(target: object, strict=True):
        ctx = bstack1ll1lll11l1_opy_.create_context(target)
        instance = bstack1lll11ll1l1_opy_.bstack1lll1llll11_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1lll111l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l11ll1l_opy_(
        ctx: bstack1llll11l1l1_opy_, state: bstack1llll1ll1ll_opy_, reverse=True
    ) -> List[bstack1111111l11_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll11ll1l1_opy_.bstack1lll1llll11_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111l111_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llll1ll1l1_opy_(instance: bstack1111111l11_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1111111l11_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll1l11l_opy_(instance: bstack1111111l11_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll11ll1l1_opy_.logger.debug(bstack1lllll1_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡰ࡫ࡹ࠾ࡽ࡮ࡩࡾࢃࠠࡷࡣ࡯ࡹࡪࡃࠢᔗ") + str(value) + bstack1lllll1_opy_ (u"ࠥࠦᔘ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll11ll1l1_opy_.bstack1ll11lll11l_opy_(target, strict)
        return bstack1lll11ll1l1_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll11ll1l1_opy_.bstack1ll11lll11l_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack1l11111l111_opy_(self):
        return self.framework_name == bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᔙ")
    def bstack1l1111111ll_opy_(self, target):
        return target if not self.bstack1l11111l111_opy_() else self.bstack1l11111l1ll_opy_()
    @staticmethod
    def bstack1l11111l1ll_opy_():
        return str(os.getpid()) + str(threading.get_ident())