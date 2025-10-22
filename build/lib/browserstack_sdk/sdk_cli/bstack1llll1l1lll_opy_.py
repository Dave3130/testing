# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1ll1llll1ll_opy_ import bstack1ll1ll11l1l_opy_, bstack1llll111l1l_opy_
import os
import threading
class bstack1lllll11l11_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l111ll_opy_ (u"ࠣࡊࡲࡳࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᔤ").format(self.name)
class bstack1llllll1111_opy_(Enum):
    NONE = 0
    bstack1lllll11111_opy_ = 1
    bstack1ll1ll1ll1l_opy_ = 3
    bstack1lllllll11l_opy_ = 4
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
        return bstack1l111ll_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡔࡶࡤࡸࡪ࠴ࡻࡾࠤᔥ").format(self.name)
class bstack1llll1ll111_opy_(bstack1ll1ll11l1l_opy_):
    framework_name: str
    framework_version: str
    state: bstack1llllll1111_opy_
    previous_state: bstack1llllll1111_opy_
    bstack1ll1lllll11_opy_: datetime
    bstack1l111111ll1_opy_: datetime
    def __init__(
        self,
        context: bstack1llll111l1l_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1llllll1111_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1llllll1111_opy_.NONE
        self.bstack1ll1lllll11_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l111111ll1_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll1ll1l_opy_(self, bstack1l11111l1l1_opy_: bstack1llllll1111_opy_):
        bstack1l111111lll_opy_ = bstack1llllll1111_opy_(bstack1l11111l1l1_opy_).name
        if not bstack1l111111lll_opy_:
            return False
        if bstack1l11111l1l1_opy_ == self.state:
            return False
        if self.state == bstack1llllll1111_opy_.bstack1ll1ll1ll1l_opy_: # bstack11lllll1ll1_opy_ bstack1l111111111_opy_ for bstack1l111111l11_opy_ in Playwright, it bstack11llllll11l_opy_ bstack1l1111111l1_opy_ multiple times bstack11llllll1l1_opy_ a new state
            return True
        if (
            bstack1l11111l1l1_opy_ == bstack1llllll1111_opy_.NONE
            or (self.state != bstack1llllll1111_opy_.NONE and bstack1l11111l1l1_opy_ == bstack1llllll1111_opy_.bstack1lllll11111_opy_)
            or (self.state < bstack1llllll1111_opy_.bstack1lllll11111_opy_ and bstack1l11111l1l1_opy_ == bstack1llllll1111_opy_.bstack1lllllll11l_opy_)
            or (self.state < bstack1llllll1111_opy_.bstack1lllll11111_opy_ and bstack1l11111l1l1_opy_ == bstack1llllll1111_opy_.QUIT)
        ):
            raise ValueError(bstack1l111ll_opy_ (u"ࠥ࡭ࡳࡼࡡ࡭࡫ࡧࠤࡸࡺࡡࡵࡧࠣࡸࡷࡧ࡮ࡴ࡫ࡷ࡭ࡴࡴ࠺ࠡࠤᔦ") + str(self.state) + bstack1l111ll_opy_ (u"ࠦࠥࡃ࠾ࠡࠤᔧ") + str(bstack1l11111l1l1_opy_))
        self.previous_state = self.state
        self.state = bstack1l11111l1l1_opy_
        self.bstack1l111111ll1_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll111lll1_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1l1111l_opy_: Dict[str, bstack1llll1ll111_opy_] = dict()
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
    def bstack1l1ll1l11l1_opy_(self, instance: bstack1llll1ll111_opy_, method_name: str, bstack1l1lll11111_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1ll1lllll_opy_(
        self, method_name, previous_state: bstack1llllll1111_opy_, *args, **kwargs
    ) -> bstack1llllll1111_opy_:
        return
    @abc.abstractmethod
    def bstack1l1lll111l1_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1ll1lll11_opy_(self, bstack11lllllll1l_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack11lllllll1l_opy_:
                bstack11llllll1ll_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack11llllll1ll_opy_):
                    self.logger.warning(bstack1l111ll_opy_ (u"ࠧࡻ࡮ࡱࡣࡷࡧ࡭࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࠥᔨ") + str(method_name) + bstack1l111ll_opy_ (u"ࠨࠢᔩ"))
                    continue
                bstack1l1ll1l1l11_opy_ = self.bstack1l1ll1lllll_opy_(
                    method_name, previous_state=bstack1llllll1111_opy_.NONE
                )
                bstack11llllll111_opy_ = self.bstack11lllllll11_opy_(
                    method_name,
                    (bstack1l1ll1l1l11_opy_ if bstack1l1ll1l1l11_opy_ else bstack1llllll1111_opy_.NONE),
                    bstack11llllll1ll_opy_,
                )
                if not callable(bstack11llllll111_opy_):
                    self.logger.warning(bstack1l111ll_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠠ࡯ࡱࡷࠤࡵࡧࡴࡤࡪࡨࡨ࠿ࠦࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࠨࡼࡵࡨࡰ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽ࠻ࠢࠥᔪ") + str(self.framework_version) + bstack1l111ll_opy_ (u"ࠣࠫࠥᔫ"))
                    continue
                setattr(clazz, method_name, bstack11llllll111_opy_)
    def bstack11lllllll11_opy_(
        self,
        method_name: str,
        bstack1l1ll1l1l11_opy_: bstack1llllll1111_opy_,
        bstack11llllll1ll_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack11111ll1ll_opy_ = datetime.now()
            (bstack1l1ll1l1l11_opy_,) = wrapped.__vars__
            bstack1l1ll1l1l11_opy_ = (
                bstack1l1ll1l1l11_opy_
                if bstack1l1ll1l1l11_opy_ and bstack1l1ll1l1l11_opy_ != bstack1llllll1111_opy_.NONE
                else self.bstack1l1ll1lllll_opy_(method_name, previous_state=bstack1l1ll1l1l11_opy_, *args, **kwargs)
            )
            if bstack1l1ll1l1l11_opy_ == bstack1llllll1111_opy_.bstack1lllll11111_opy_:
                ctx = bstack1ll1ll11l1l_opy_.create_context(self.bstack11lllllllll_opy_(target))
                if not self.bstack1l11111111l_opy_() or ctx.id not in bstack1lll111lll1_opy_.bstack1lll1l1111l_opy_:
                    bstack1lll111lll1_opy_.bstack1lll1l1111l_opy_[ctx.id] = bstack1llll1ll111_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1ll1l1l11_opy_
                    )
                self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡺࡶࡦࡶࡰࡦࡦࠣࡱࡪࡺࡨࡰࡦࠣࡧࡷ࡫ࡡࡵࡧࡧ࠾ࠥࢁࡴࡢࡴࡪࡩࡹ࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡤࡶࡻࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥᔬ") + str(bstack1lll111lll1_opy_.bstack1lll1l1111l_opy_.keys()) + bstack1l111ll_opy_ (u"ࠥࠦᔭ"))
            else:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡼࡸࡡࡱࡲࡨࡨࠥࡳࡥࡵࡪࡲࡨࠥ࡯࡮ࡷࡱ࡮ࡩࡩࡀࠠࡼࡶࡤࡶ࡬࡫ࡴ࠯ࡡࡢࡧࡱࡧࡳࡴࡡࡢࢁࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨᔮ") + str(bstack1lll111lll1_opy_.bstack1lll1l1111l_opy_.keys()) + bstack1l111ll_opy_ (u"ࠧࠨᔯ"))
            instance = bstack1lll111lll1_opy_.bstack1ll11lll111_opy_(self.bstack11lllllllll_opy_(target))
            if bstack1l1ll1l1l11_opy_ == bstack1llllll1111_opy_.NONE or not instance:
                ctx = bstack1ll1ll11l1l_opy_.create_context(self.bstack11lllllllll_opy_(target))
                self.logger.warning(bstack1l111ll_opy_ (u"ࠨࡷࡳࡣࡳࡴࡪࡪࠠ࡮ࡧࡷ࡬ࡴࡪࠠࡶࡰࡷࡶࡦࡩ࡫ࡦࡦ࠽ࠤࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡧࡹࡾ࠽ࡼࡥࡷࡼࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥᔰ") + str(bstack1lll111lll1_opy_.bstack1lll1l1111l_opy_.keys()) + bstack1l111ll_opy_ (u"ࠢࠣᔱ"))
                return bstack11llllll1ll_opy_(target, *args, **kwargs)
            bstack1l1ll11ll1l_opy_ = self.bstack1l1lll111l1_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1l1l11_opy_, bstack1lllll11l11_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1lllll1ll1l_opy_(bstack1l1ll1l1l11_opy_):
                self.logger.debug(bstack1l111ll_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡥࡥࠢࡶࡸࡦࡺࡥ࠮ࡶࡵࡥࡳࡹࡩࡵ࡫ࡲࡲ࠿ࠦࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡳࡶࡪࡼࡩࡰࡷࡶࡣࡸࡺࡡࡵࡧࢀࠤࡂࡄࠠࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡷࡹࡧࡴࡦࡿࠣࠬࢀࡺࡹࡱࡧࠫࡸࡦࡸࡧࡦࡶࠬࢁ࠳ࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥࢁࡡࡳࡩࡶࢁ࠮࡛ࠦࠣᔲ") + str(instance.ref()) + bstack1l111ll_opy_ (u"ࠤࡠࠦᔳ"))
            result = (
                bstack1l1ll11ll1l_opy_(target, bstack11llllll1ll_opy_, *args, **kwargs)
                if callable(bstack1l1ll11ll1l_opy_)
                else bstack11llllll1ll_opy_(target, *args, **kwargs)
            )
            bstack11lllll1lll_opy_ = self.bstack1l1lll111l1_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1l1l11_opy_, bstack1lllll11l11_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1ll1l11l1_opy_(instance, method_name, datetime.now() - bstack11111ll1ll_opy_, *args, **kwargs)
            return bstack11lllll1lll_opy_ if bstack11lllll1lll_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1ll1l1l11_opy_,)
        return wrapped
    @staticmethod
    def bstack1ll11lll111_opy_(target: object, strict=True):
        ctx = bstack1ll1ll11l1l_opy_.create_context(target)
        instance = bstack1lll111lll1_opy_.bstack1lll1l1111l_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll11l11_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1ll11l_opy_(
        ctx: bstack1llll111l1l_opy_, state: bstack1llllll1111_opy_, reverse=True
    ) -> List[bstack1llll1ll111_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll111lll1_opy_.bstack1lll1l1111l_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lllll11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llll1l1111_opy_(instance: bstack1llll1ll111_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llll1ll111_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll1ll1l_opy_(instance: bstack1llll1ll111_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll111lll1_opy_.logger.debug(bstack1l111ll_opy_ (u"ࠥࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥࡱࡥࡺ࠿ࡾ࡯ࡪࡿࡽࠡࡸࡤࡰࡺ࡫࠽ࠣᔴ") + str(value) + bstack1l111ll_opy_ (u"ࠦࠧᔵ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll111lll1_opy_.bstack1ll11lll111_opy_(target, strict)
        return bstack1lll111lll1_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll111lll1_opy_.bstack1ll11lll111_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack1l11111111l_opy_(self):
        return self.framework_name == bstack1l111ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᔶ")
    def bstack11lllllllll_opy_(self, target):
        return target if not self.bstack1l11111111l_opy_() else self.bstack11llllllll1_opy_()
    @staticmethod
    def bstack11llllllll1_opy_():
        return str(os.getpid()) + str(threading.get_ident())