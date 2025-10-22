# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1ll1lll1ll1_opy_ import bstack1ll1ll11ll1_opy_, bstack1lll1ll1l1l_opy_
import os
import threading
class bstack1llllll1l11_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1lllll1l_opy_ (u"ࠦࡍࡵ࡯࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥᔧ").format(self.name)
class bstack1lllllll1l1_opy_(Enum):
    NONE = 0
    bstack1lllll11111_opy_ = 1
    bstack1ll1lll11l1_opy_ = 3
    bstack1lllll11l1l_opy_ = 4
    bstack1l111111l11_opy_ = 5
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
        return bstack1lllll1l_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᔨ").format(self.name)
class bstack1lllll111l1_opy_(bstack1ll1ll11ll1_opy_):
    framework_name: str
    framework_version: str
    state: bstack1lllllll1l1_opy_
    previous_state: bstack1lllllll1l1_opy_
    bstack1ll1llllll1_opy_: datetime
    bstack1l11111l1l1_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1ll1l1l_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1lllllll1l1_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1lllllll1l1_opy_.NONE
        self.bstack1ll1llllll1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l11111l1l1_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll11ll1l_opy_(self, bstack1l11111l11l_opy_: bstack1lllllll1l1_opy_):
        bstack1l11111l111_opy_ = bstack1lllllll1l1_opy_(bstack1l11111l11l_opy_).name
        if not bstack1l11111l111_opy_:
            return False
        if bstack1l11111l11l_opy_ == self.state:
            return False
        if self.state == bstack1lllllll1l1_opy_.bstack1ll1lll11l1_opy_: # bstack1l11111111l_opy_ bstack1l1111111ll_opy_ for bstack11llllll11l_opy_ in Playwright, it bstack11llllll111_opy_ bstack1l111111ll1_opy_ multiple times bstack1l111111l1l_opy_ a new state
            return True
        if (
            bstack1l11111l11l_opy_ == bstack1lllllll1l1_opy_.NONE
            or (self.state != bstack1lllllll1l1_opy_.NONE and bstack1l11111l11l_opy_ == bstack1lllllll1l1_opy_.bstack1lllll11111_opy_)
            or (self.state < bstack1lllllll1l1_opy_.bstack1lllll11111_opy_ and bstack1l11111l11l_opy_ == bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_)
            or (self.state < bstack1lllllll1l1_opy_.bstack1lllll11111_opy_ and bstack1l11111l11l_opy_ == bstack1lllllll1l1_opy_.QUIT)
        ):
            raise ValueError(bstack1lllll1l_opy_ (u"ࠨࡩ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡶࡤࡸࡪࠦࡴࡳࡣࡱࡷ࡮ࡺࡩࡰࡰ࠽ࠤࠧᔩ") + str(self.state) + bstack1lllll1l_opy_ (u"ࠢࠡ࠿ࡁࠤࠧᔪ") + str(bstack1l11111l11l_opy_))
        self.previous_state = self.state
        self.state = bstack1l11111l11l_opy_
        self.bstack1l11111l1l1_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll1111l1l_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll11lllll_opy_: Dict[str, bstack1lllll111l1_opy_] = dict()
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
    def bstack1l1ll1l1l1l_opy_(self, instance: bstack1lllll111l1_opy_, method_name: str, bstack1l1ll1ll1ll_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1lll1l11l_opy_(
        self, method_name, previous_state: bstack1lllllll1l1_opy_, *args, **kwargs
    ) -> bstack1lllllll1l1_opy_:
        return
    @abc.abstractmethod
    def bstack1l1ll1lll11_opy_(
        self,
        target: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1lll11lll_opy_(self, bstack11lllllllll_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack11lllllllll_opy_:
                bstack11llllllll1_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack11llllllll1_opy_):
                    self.logger.warning(bstack1lllll1l_opy_ (u"ࠣࡷࡱࡴࡦࡺࡣࡩࡧࡧࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠥࠨᔫ") + str(method_name) + bstack1lllll1l_opy_ (u"ࠤࠥᔬ"))
                    continue
                bstack1l1lll111l1_opy_ = self.bstack1l1lll1l11l_opy_(
                    method_name, previous_state=bstack1lllllll1l1_opy_.NONE
                )
                bstack11llllll1ll_opy_ = self.bstack1l111111111_opy_(
                    method_name,
                    (bstack1l1lll111l1_opy_ if bstack1l1lll111l1_opy_ else bstack1lllllll1l1_opy_.NONE),
                    bstack11llllllll1_opy_,
                )
                if not callable(bstack11llllll1ll_opy_):
                    self.logger.warning(bstack1lllll1l_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠣࡲࡴࡺࠠࡱࡣࡷࡧ࡭࡫ࡤ࠻ࠢࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࠫࡿࡸ࡫࡬ࡧ࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࢀ࠾ࠥࠨᔭ") + str(self.framework_version) + bstack1lllll1l_opy_ (u"ࠦ࠮ࠨᔮ"))
                    continue
                setattr(clazz, method_name, bstack11llllll1ll_opy_)
    def bstack1l111111111_opy_(
        self,
        method_name: str,
        bstack1l1lll111l1_opy_: bstack1lllllll1l1_opy_,
        bstack11llllllll1_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1ll111ll1_opy_ = datetime.now()
            (bstack1l1lll111l1_opy_,) = wrapped.__vars__
            bstack1l1lll111l1_opy_ = (
                bstack1l1lll111l1_opy_
                if bstack1l1lll111l1_opy_ and bstack1l1lll111l1_opy_ != bstack1lllllll1l1_opy_.NONE
                else self.bstack1l1lll1l11l_opy_(method_name, previous_state=bstack1l1lll111l1_opy_, *args, **kwargs)
            )
            if bstack1l1lll111l1_opy_ == bstack1lllllll1l1_opy_.bstack1lllll11111_opy_:
                ctx = bstack1ll1ll11ll1_opy_.create_context(self.bstack11lllllll11_opy_(target))
                if not self.bstack1l1111111l1_opy_() or ctx.id not in bstack1lll1111l1l_opy_.bstack1lll11lllll_opy_:
                    bstack1lll1111l1l_opy_.bstack1lll11lllll_opy_[ctx.id] = bstack1lllll111l1_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1lll111l1_opy_
                    )
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡣࡳࡧࡤࡸࡪࡪ࠺ࠡࡽࡷࡥࡷ࡭ࡥࡵ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡧࡹࡾ࠽ࡼࡥࡷࡼ࠳࡯ࡤࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨᔯ") + str(bstack1lll1111l1l_opy_.bstack1lll11lllll_opy_.keys()) + bstack1lllll1l_opy_ (u"ࠨࠢᔰ"))
            else:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡸࡴࡤࡴࡵ࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤࠡ࡫ࡱࡺࡴࡱࡥࡥ࠼ࠣࡿࡹࡧࡲࡨࡧࡷ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᔱ") + str(bstack1lll1111l1l_opy_.bstack1lll11lllll_opy_.keys()) + bstack1lllll1l_opy_ (u"ࠣࠤᔲ"))
            instance = bstack1lll1111l1l_opy_.bstack1l1llllllll_opy_(self.bstack11lllllll11_opy_(target))
            if bstack1l1lll111l1_opy_ == bstack1lllllll1l1_opy_.NONE or not instance:
                ctx = bstack1ll1ll11ll1_opy_.create_context(self.bstack11lllllll11_opy_(target))
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠤࡺࡶࡦࡶࡰࡦࡦࠣࡱࡪࡺࡨࡰࡦࠣࡹࡳࡺࡲࡢࡥ࡮ࡩࡩࡀࠠࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡣࡵࡺࡀࡿࡨࡺࡸࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨᔳ") + str(bstack1lll1111l1l_opy_.bstack1lll11lllll_opy_.keys()) + bstack1lllll1l_opy_ (u"ࠥࠦᔴ"))
                return bstack11llllllll1_opy_(target, *args, **kwargs)
            bstack1l1ll111l1l_opy_ = self.bstack1l1ll1lll11_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll111l1_opy_, bstack1llllll1l11_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1llll11ll1l_opy_(bstack1l1lll111l1_opy_):
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡨࡨࠥࡹࡴࡢࡶࡨ࠱ࡹࡸࡡ࡯ࡵ࡬ࡸ࡮ࡵ࡮࠻ࠢࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡶࡲࡦࡸ࡬ࡳࡺࡹ࡟ࡴࡶࡤࡸࡪࢃࠠ࠾ࡀࠣࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡳࡵࡣࡷࡩࢂࠦࠨࡼࡶࡼࡴࡪ࠮ࡴࡢࡴࡪࡩࡹ࠯ࡽ࠯ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡽࡤࡶ࡬ࡹࡽࠪࠢ࡞ࠦᔵ") + str(instance.ref()) + bstack1lllll1l_opy_ (u"ࠧࡣࠢᔶ"))
            result = (
                bstack1l1ll111l1l_opy_(target, bstack11llllllll1_opy_, *args, **kwargs)
                if callable(bstack1l1ll111l1l_opy_)
                else bstack11llllllll1_opy_(target, *args, **kwargs)
            )
            bstack11lllllll1l_opy_ = self.bstack1l1ll1lll11_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll111l1_opy_, bstack1llllll1l11_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1ll1l1l1l_opy_(instance, method_name, datetime.now() - bstack1ll111ll1_opy_, *args, **kwargs)
            return bstack11lllllll1l_opy_ if bstack11lllllll1l_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1lll111l1_opy_,)
        return wrapped
    @staticmethod
    def bstack1l1llllllll_opy_(target: object, strict=True):
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        instance = bstack1lll1111l1l_opy_.bstack1lll11lllll_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll11l1l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l111lll_opy_(
        ctx: bstack1lll1ll1l1l_opy_, state: bstack1lllllll1l1_opy_, reverse=True
    ) -> List[bstack1lllll111l1_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll1111l1l_opy_.bstack1lll11lllll_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1llllll1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllllll11l_opy_(instance: bstack1lllll111l1_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lllll111l1_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll11ll1l_opy_(instance: bstack1lllll111l1_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll1111l1l_opy_.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡴࡨࡪ࠭࠯ࡽࠡ࡭ࡨࡽࡂࢁ࡫ࡦࡻࢀࠤࡻࡧ࡬ࡶࡧࡀࠦᔷ") + str(value) + bstack1lllll1l_opy_ (u"ࠢࠣᔸ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll1111l1l_opy_.bstack1l1llllllll_opy_(target, strict)
        return bstack1lll1111l1l_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll1111l1l_opy_.bstack1l1llllllll_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack1l1111111l1_opy_(self):
        return self.framework_name == bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᔹ")
    def bstack11lllllll11_opy_(self, target):
        return target if not self.bstack1l1111111l1_opy_() else self.bstack11llllll1l1_opy_()
    @staticmethod
    def bstack11llllll1l1_opy_():
        return str(os.getpid()) + str(threading.get_ident())