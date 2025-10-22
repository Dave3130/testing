# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1ll1lllll1l_opy_ import bstack1ll1ll11l1l_opy_, bstack1lll1l111l1_opy_
import os
import threading
class bstack1lllll1l1ll_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack111l1l_opy_ (u"ࠣࡊࡲࡳࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᔤ").format(self.name)
class bstack1llll1lll1l_opy_(Enum):
    NONE = 0
    bstack1llllllllll_opy_ = 1
    bstack1ll1ll1l111_opy_ = 3
    bstack1llllll1lll_opy_ = 4
    bstack11llllll1ll_opy_ = 5
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
        return bstack111l1l_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡔࡶࡤࡸࡪ࠴ࡻࡾࠤᔥ").format(self.name)
class bstack1lllllll1l1_opy_(bstack1ll1ll11l1l_opy_):
    framework_name: str
    framework_version: str
    state: bstack1llll1lll1l_opy_
    previous_state: bstack1llll1lll1l_opy_
    bstack1ll1lllll11_opy_: datetime
    bstack1l11111l111_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1l111l1_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1llll1lll1l_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1llll1lll1l_opy_.NONE
        self.bstack1ll1lllll11_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l11111l111_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll1l111l_opy_(self, bstack1l111111lll_opy_: bstack1llll1lll1l_opy_):
        bstack1l111111l1l_opy_ = bstack1llll1lll1l_opy_(bstack1l111111lll_opy_).name
        if not bstack1l111111l1l_opy_:
            return False
        if bstack1l111111lll_opy_ == self.state:
            return False
        if self.state == bstack1llll1lll1l_opy_.bstack1ll1ll1l111_opy_: # bstack11lllllll1l_opy_ bstack1l111111111_opy_ for bstack11lllllllll_opy_ in Playwright, it bstack1l1111111l1_opy_ bstack11lllllll11_opy_ multiple times bstack1l11111111l_opy_ a new state
            return True
        if (
            bstack1l111111lll_opy_ == bstack1llll1lll1l_opy_.NONE
            or (self.state != bstack1llll1lll1l_opy_.NONE and bstack1l111111lll_opy_ == bstack1llll1lll1l_opy_.bstack1llllllllll_opy_)
            or (self.state < bstack1llll1lll1l_opy_.bstack1llllllllll_opy_ and bstack1l111111lll_opy_ == bstack1llll1lll1l_opy_.bstack1llllll1lll_opy_)
            or (self.state < bstack1llll1lll1l_opy_.bstack1llllllllll_opy_ and bstack1l111111lll_opy_ == bstack1llll1lll1l_opy_.QUIT)
        ):
            raise ValueError(bstack111l1l_opy_ (u"ࠥ࡭ࡳࡼࡡ࡭࡫ࡧࠤࡸࡺࡡࡵࡧࠣࡸࡷࡧ࡮ࡴ࡫ࡷ࡭ࡴࡴ࠺ࠡࠤᔦ") + str(self.state) + bstack111l1l_opy_ (u"ࠦࠥࡃ࠾ࠡࠤᔧ") + str(bstack1l111111lll_opy_))
        self.previous_state = self.state
        self.state = bstack1l111111lll_opy_
        self.bstack1l11111l111_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll111l1l1_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll1ll11l1_opy_: Dict[str, bstack1lllllll1l1_opy_] = dict()
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
    def bstack1l1ll1l11l1_opy_(self, instance: bstack1lllllll1l1_opy_, method_name: str, bstack1l1lll11lll_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1ll1l1l1l_opy_(
        self, method_name, previous_state: bstack1llll1lll1l_opy_, *args, **kwargs
    ) -> bstack1llll1lll1l_opy_:
        return
    @abc.abstractmethod
    def bstack1l1ll1l1ll1_opy_(
        self,
        target: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1lll111l1_opy_(self, bstack1l1111111ll_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack1l1111111ll_opy_:
                bstack11llllll111_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack11llllll111_opy_):
                    self.logger.warning(bstack111l1l_opy_ (u"ࠧࡻ࡮ࡱࡣࡷࡧ࡭࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࠥᔨ") + str(method_name) + bstack111l1l_opy_ (u"ࠨࠢᔩ"))
                    continue
                bstack1l1lll111ll_opy_ = self.bstack1l1ll1l1l1l_opy_(
                    method_name, previous_state=bstack1llll1lll1l_opy_.NONE
                )
                bstack11llllllll1_opy_ = self.bstack11lllll1lll_opy_(
                    method_name,
                    (bstack1l1lll111ll_opy_ if bstack1l1lll111ll_opy_ else bstack1llll1lll1l_opy_.NONE),
                    bstack11llllll111_opy_,
                )
                if not callable(bstack11llllllll1_opy_):
                    self.logger.warning(bstack111l1l_opy_ (u"ࠢ࡮ࡧࡷ࡬ࡴࡪࠠ࡯ࡱࡷࠤࡵࡧࡴࡤࡪࡨࡨ࠿ࠦࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࠨࡼࡵࡨࡰ࡫࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࡽ࠻ࠢࠥᔪ") + str(self.framework_version) + bstack111l1l_opy_ (u"ࠣࠫࠥᔫ"))
                    continue
                setattr(clazz, method_name, bstack11llllllll1_opy_)
    def bstack11lllll1lll_opy_(
        self,
        method_name: str,
        bstack1l1lll111ll_opy_: bstack1llll1lll1l_opy_,
        bstack11llllll111_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1l1ll111ll_opy_ = datetime.now()
            (bstack1l1lll111ll_opy_,) = wrapped.__vars__
            bstack1l1lll111ll_opy_ = (
                bstack1l1lll111ll_opy_
                if bstack1l1lll111ll_opy_ and bstack1l1lll111ll_opy_ != bstack1llll1lll1l_opy_.NONE
                else self.bstack1l1ll1l1l1l_opy_(method_name, previous_state=bstack1l1lll111ll_opy_, *args, **kwargs)
            )
            if bstack1l1lll111ll_opy_ == bstack1llll1lll1l_opy_.bstack1llllllllll_opy_:
                ctx = bstack1ll1ll11l1l_opy_.create_context(self.bstack11lllll1ll1_opy_(target))
                if not self.bstack11llllll1l1_opy_() or ctx.id not in bstack1lll111l1l1_opy_.bstack1lll1ll11l1_opy_:
                    bstack1lll111l1l1_opy_.bstack1lll1ll11l1_opy_[ctx.id] = bstack1lllllll1l1_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1lll111ll_opy_
                    )
                self.logger.debug(bstack111l1l_opy_ (u"ࠤࡺࡶࡦࡶࡰࡦࡦࠣࡱࡪࡺࡨࡰࡦࠣࡧࡷ࡫ࡡࡵࡧࡧ࠾ࠥࢁࡴࡢࡴࡪࡩࡹ࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡤࡶࡻࡁࢀࡩࡴࡹ࠰࡬ࡨࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥᔬ") + str(bstack1lll111l1l1_opy_.bstack1lll1ll11l1_opy_.keys()) + bstack111l1l_opy_ (u"ࠥࠦᔭ"))
            else:
                self.logger.debug(bstack111l1l_opy_ (u"ࠦࡼࡸࡡࡱࡲࡨࡨࠥࡳࡥࡵࡪࡲࡨࠥ࡯࡮ࡷࡱ࡮ࡩࡩࡀࠠࡼࡶࡤࡶ࡬࡫ࡴ࠯ࡡࡢࡧࡱࡧࡳࡴࡡࡢࢁࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࡂࠨᔮ") + str(bstack1lll111l1l1_opy_.bstack1lll1ll11l1_opy_.keys()) + bstack111l1l_opy_ (u"ࠧࠨᔯ"))
            instance = bstack1lll111l1l1_opy_.bstack1l1llll111l_opy_(self.bstack11lllll1ll1_opy_(target))
            if bstack1l1lll111ll_opy_ == bstack1llll1lll1l_opy_.NONE or not instance:
                ctx = bstack1ll1ll11l1l_opy_.create_context(self.bstack11lllll1ll1_opy_(target))
                self.logger.warning(bstack111l1l_opy_ (u"ࠨࡷࡳࡣࡳࡴࡪࡪࠠ࡮ࡧࡷ࡬ࡴࡪࠠࡶࡰࡷࡶࡦࡩ࡫ࡦࡦ࠽ࠤࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡧࡹࡾ࠽ࡼࡥࡷࡼࢂࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࡴ࠿ࠥᔰ") + str(bstack1lll111l1l1_opy_.bstack1lll1ll11l1_opy_.keys()) + bstack111l1l_opy_ (u"ࠢࠣᔱ"))
                return bstack11llllll111_opy_(target, *args, **kwargs)
            bstack1l1ll111lll_opy_ = self.bstack1l1ll1l1ll1_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll111ll_opy_, bstack1lllll1l1ll_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1llll1l111l_opy_(bstack1l1lll111ll_opy_):
                self.logger.debug(bstack111l1l_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡥࡥࠢࡶࡸࡦࡺࡥ࠮ࡶࡵࡥࡳࡹࡩࡵ࡫ࡲࡲ࠿ࠦࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡳࡶࡪࡼࡩࡰࡷࡶࡣࡸࡺࡡࡵࡧࢀࠤࡂࡄࠠࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡷࡹࡧࡴࡦࡿࠣࠬࢀࡺࡹࡱࡧࠫࡸࡦࡸࡧࡦࡶࠬࢁ࠳ࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥࢁࡡࡳࡩࡶࢁ࠮࡛ࠦࠣᔲ") + str(instance.ref()) + bstack111l1l_opy_ (u"ࠤࡠࠦᔳ"))
            result = (
                bstack1l1ll111lll_opy_(target, bstack11llllll111_opy_, *args, **kwargs)
                if callable(bstack1l1ll111lll_opy_)
                else bstack11llllll111_opy_(target, *args, **kwargs)
            )
            bstack1l111111l11_opy_ = self.bstack1l1ll1l1ll1_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll111ll_opy_, bstack1lllll1l1ll_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1ll1l11l1_opy_(instance, method_name, datetime.now() - bstack1l1ll111ll_opy_, *args, **kwargs)
            return bstack1l111111l11_opy_ if bstack1l111111l11_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1lll111ll_opy_,)
        return wrapped
    @staticmethod
    def bstack1l1llll111l_opy_(target: object, strict=True):
        ctx = bstack1ll1ll11l1l_opy_.create_context(target)
        instance = bstack1lll111l1l1_opy_.bstack1lll1ll11l1_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll111l1_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1111ll_opy_(
        ctx: bstack1lll1l111l1_opy_, state: bstack1llll1lll1l_opy_, reverse=True
    ) -> List[bstack1lllllll1l1_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll111l1l1_opy_.bstack1lll1ll11l1_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lllll11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1llll1l1l11_opy_(instance: bstack1lllllll1l1_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lllllll1l1_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll1l111l_opy_(instance: bstack1lllllll1l1_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll111l1l1_opy_.logger.debug(bstack111l1l_opy_ (u"ࠥࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥࡱࡥࡺ࠿ࡾ࡯ࡪࡿࡽࠡࡸࡤࡰࡺ࡫࠽ࠣᔴ") + str(value) + bstack111l1l_opy_ (u"ࠦࠧᔵ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll111l1l1_opy_.bstack1l1llll111l_opy_(target, strict)
        return bstack1lll111l1l1_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll111l1l1_opy_.bstack1l1llll111l_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack11llllll1l1_opy_(self):
        return self.framework_name == bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᔶ")
    def bstack11lllll1ll1_opy_(self, target):
        return target if not self.bstack11llllll1l1_opy_() else self.bstack11llllll11l_opy_()
    @staticmethod
    def bstack11llllll11l_opy_():
        return str(os.getpid()) + str(threading.get_ident())