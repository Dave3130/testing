# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1ll1ll11ll1_opy_, bstack1lll1lllll1_opy_
import os
import threading
class bstack1llll1l1lll_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack11l111_opy_ (u"ࠨࡈࡰࡱ࡮ࡗࡹࡧࡴࡦ࠰ࡾࢁࠧᔩ").format(self.name)
class bstack1lllll1lll1_opy_(Enum):
    NONE = 0
    bstack1llll11llll_opy_ = 1
    bstack1ll1ll1l11l_opy_ = 3
    bstack1llllll11l1_opy_ = 4
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
        return bstack11l111_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡶࡨ࠲ࢀࢃࠢᔪ").format(self.name)
class bstack1llll1l1111_opy_(bstack1ll1ll11ll1_opy_):
    framework_name: str
    framework_version: str
    state: bstack1lllll1lll1_opy_
    previous_state: bstack1lllll1lll1_opy_
    bstack1ll1lllll11_opy_: datetime
    bstack1l11111l111_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1lllll1_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1lllll1lll1_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1lllll1lll1_opy_.NONE
        self.bstack1ll1lllll11_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l11111l111_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llllllll1l_opy_(self, bstack1l11111ll11_opy_: bstack1lllll1lll1_opy_):
        bstack1l111111lll_opy_ = bstack1lllll1lll1_opy_(bstack1l11111ll11_opy_).name
        if not bstack1l111111lll_opy_:
            return False
        if bstack1l11111ll11_opy_ == self.state:
            return False
        if self.state == bstack1lllll1lll1_opy_.bstack1ll1ll1l11l_opy_: # bstack1l111111ll1_opy_ bstack11llllll1ll_opy_ for bstack11llllll111_opy_ in Playwright, it bstack11llllll11l_opy_ bstack11lllllll11_opy_ multiple times bstack11lllllllll_opy_ a new state
            return True
        if (
            bstack1l11111ll11_opy_ == bstack1lllll1lll1_opy_.NONE
            or (self.state != bstack1lllll1lll1_opy_.NONE and bstack1l11111ll11_opy_ == bstack1lllll1lll1_opy_.bstack1llll11llll_opy_)
            or (self.state < bstack1lllll1lll1_opy_.bstack1llll11llll_opy_ and bstack1l11111ll11_opy_ == bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_)
            or (self.state < bstack1lllll1lll1_opy_.bstack1llll11llll_opy_ and bstack1l11111ll11_opy_ == bstack1lllll1lll1_opy_.QUIT)
        ):
            raise ValueError(bstack11l111_opy_ (u"ࠣ࡫ࡱࡺࡦࡲࡩࡥࠢࡶࡸࡦࡺࡥࠡࡶࡵࡥࡳࡹࡩࡵ࡫ࡲࡲ࠿ࠦࠢᔫ") + str(self.state) + bstack11l111_opy_ (u"ࠤࠣࡁࡃࠦࠢᔬ") + str(bstack1l11111ll11_opy_))
        self.previous_state = self.state
        self.state = bstack1l11111ll11_opy_
        self.bstack1l11111l111_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll11l1111_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1lll11llll1_opy_: Dict[str, bstack1llll1l1111_opy_] = dict()
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
    def bstack1l1lll1l111_opy_(self, instance: bstack1llll1l1111_opy_, method_name: str, bstack1l1lll111ll_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1lll11l1l_opy_(
        self, method_name, previous_state: bstack1lllll1lll1_opy_, *args, **kwargs
    ) -> bstack1lllll1lll1_opy_:
        return
    @abc.abstractmethod
    def bstack1l1ll1l1lll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1lll11111_opy_(self, bstack11llllllll1_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack11llllllll1_opy_:
                bstack1l111111111_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1l111111111_opy_):
                    self.logger.warning(bstack11l111_opy_ (u"ࠥࡹࡳࡶࡡࡵࡥ࡫ࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࠣᔭ") + str(method_name) + bstack11l111_opy_ (u"ࠦࠧᔮ"))
                    continue
                bstack1l1ll1l1ll1_opy_ = self.bstack1l1lll11l1l_opy_(
                    method_name, previous_state=bstack1lllll1lll1_opy_.NONE
                )
                bstack11lllllll1l_opy_ = self.bstack1l11111111l_opy_(
                    method_name,
                    (bstack1l1ll1l1ll1_opy_ if bstack1l1ll1l1ll1_opy_ else bstack1lllll1lll1_opy_.NONE),
                    bstack1l111111111_opy_,
                )
                if not callable(bstack11lllllll1l_opy_):
                    self.logger.warning(bstack11l111_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࠥࡴ࡯ࡵࠢࡳࡥࡹࡩࡨࡦࡦ࠽ࠤࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࠭ࢁࡳࡦ࡮ࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࡀࠠࠣᔯ") + str(self.framework_version) + bstack11l111_opy_ (u"ࠨࠩࠣᔰ"))
                    continue
                setattr(clazz, method_name, bstack11lllllll1l_opy_)
    def bstack1l11111111l_opy_(
        self,
        method_name: str,
        bstack1l1ll1l1ll1_opy_: bstack1lllll1lll1_opy_,
        bstack1l111111111_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1l1ll1ll1_opy_ = datetime.now()
            (bstack1l1ll1l1ll1_opy_,) = wrapped.__vars__
            bstack1l1ll1l1ll1_opy_ = (
                bstack1l1ll1l1ll1_opy_
                if bstack1l1ll1l1ll1_opy_ and bstack1l1ll1l1ll1_opy_ != bstack1lllll1lll1_opy_.NONE
                else self.bstack1l1lll11l1l_opy_(method_name, previous_state=bstack1l1ll1l1ll1_opy_, *args, **kwargs)
            )
            if bstack1l1ll1l1ll1_opy_ == bstack1lllll1lll1_opy_.bstack1llll11llll_opy_:
                ctx = bstack1ll1ll11ll1_opy_.create_context(self.bstack11llllll1l1_opy_(target))
                if not self.bstack1l1111111ll_opy_() or ctx.id not in bstack1lll11l1111_opy_.bstack1lll11llll1_opy_:
                    bstack1lll11l1111_opy_.bstack1lll11llll1_opy_[ctx.id] = bstack1llll1l1111_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1ll1l1ll1_opy_
                    )
                self.logger.debug(bstack11l111_opy_ (u"ࠢࡸࡴࡤࡴࡵ࡫ࡤࠡ࡯ࡨࡸ࡭ࡵࡤࠡࡥࡵࡩࡦࡺࡥࡥ࠼ࠣࡿࡹࡧࡲࡨࡧࡷ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡩࡴࡹ࠿ࡾࡧࡹࡾ࠮ࡪࡦࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡹ࠽ࠣᔱ") + str(bstack1lll11l1111_opy_.bstack1lll11llll1_opy_.keys()) + bstack11l111_opy_ (u"ࠣࠤᔲ"))
            else:
                self.logger.debug(bstack11l111_opy_ (u"ࠤࡺࡶࡦࡶࡰࡦࡦࠣࡱࡪࡺࡨࡰࡦࠣ࡭ࡳࡼ࡯࡬ࡧࡧ࠾ࠥࢁࡴࡢࡴࡪࡩࡹ࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦࡵࡀࠦᔳ") + str(bstack1lll11l1111_opy_.bstack1lll11llll1_opy_.keys()) + bstack11l111_opy_ (u"ࠥࠦᔴ"))
            instance = bstack1lll11l1111_opy_.bstack1ll111lll1l_opy_(self.bstack11llllll1l1_opy_(target))
            if bstack1l1ll1l1ll1_opy_ == bstack1lllll1lll1_opy_.NONE or not instance:
                ctx = bstack1ll1ll11ll1_opy_.create_context(self.bstack11llllll1l1_opy_(target))
                self.logger.warning(bstack11l111_opy_ (u"ࠦࡼࡸࡡࡱࡲࡨࡨࠥࡳࡥࡵࡪࡲࡨࠥࡻ࡮ࡵࡴࡤࡧࡰ࡫ࡤ࠻ࠢࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡥࡷࡼࡂࢁࡣࡵࡺࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡹ࠽ࠣᔵ") + str(bstack1lll11l1111_opy_.bstack1lll11llll1_opy_.keys()) + bstack11l111_opy_ (u"ࠧࠨᔶ"))
                return bstack1l111111111_opy_(target, *args, **kwargs)
            bstack1l1ll11l11l_opy_ = self.bstack1l1ll1l1lll_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1l1ll1_opy_, bstack1llll1l1lll_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1llllllll1l_opy_(bstack1l1ll1l1ll1_opy_):
                self.logger.debug(bstack11l111_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡪࡪࠠࡴࡶࡤࡸࡪ࠳ࡴࡳࡣࡱࡷ࡮ࡺࡩࡰࡰ࠽ࠤࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡱࡴࡨࡺ࡮ࡵࡵࡴࡡࡶࡸࡦࡺࡥࡾࠢࡀࡂࠥࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡵࡷࡥࡹ࡫ࡽࠡࠪࡾࡸࡾࡶࡥࠩࡶࡤࡶ࡬࡫ࡴࠪࡿ࠱ࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡿࡦࡸࡧࡴࡿࠬࠤࡠࠨᔷ") + str(instance.ref()) + bstack11l111_opy_ (u"ࠢ࡞ࠤᔸ"))
            result = (
                bstack1l1ll11l11l_opy_(target, bstack1l111111111_opy_, *args, **kwargs)
                if callable(bstack1l1ll11l11l_opy_)
                else bstack1l111111111_opy_(target, *args, **kwargs)
            )
            bstack1l111111l1l_opy_ = self.bstack1l1ll1l1lll_opy_(
                target,
                (instance, method_name),
                (bstack1l1ll1l1ll1_opy_, bstack1llll1l1lll_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1lll1l111_opy_(instance, method_name, datetime.now() - bstack1l1ll1ll1_opy_, *args, **kwargs)
            return bstack1l111111l1l_opy_ if bstack1l111111l1l_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1ll1l1ll1_opy_,)
        return wrapped
    @staticmethod
    def bstack1ll111lll1l_opy_(target: object, strict=True):
        ctx = bstack1ll1ll11ll1_opy_.create_context(target)
        instance = bstack1lll11l1111_opy_.bstack1lll11llll1_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll11l11_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l111lll1l1_opy_(
        ctx: bstack1lll1lllll1_opy_, state: bstack1lllll1lll1_opy_, reverse=True
    ) -> List[bstack1llll1l1111_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll11l1111_opy_.bstack1lll11llll1_opy_.values(),
            ),
            key=lambda t: t.bstack1ll1lllll11_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllllll1ll_opy_(instance: bstack1llll1l1111_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1llll1l1111_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llllllll1l_opy_(instance: bstack1llll1l1111_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll11l1111_opy_.logger.debug(bstack11l111_opy_ (u"ࠣࡵࡨࡸࡤࡹࡴࡢࡶࡨ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼ࡫ࡱࡷࡹࡧ࡮ࡤࡧ࠱ࡶࡪ࡬ࠨࠪࡿࠣ࡯ࡪࡿ࠽ࡼ࡭ࡨࡽࢂࠦࡶࡢ࡮ࡸࡩࡂࠨᔹ") + str(value) + bstack11l111_opy_ (u"ࠤࠥᔺ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll11l1111_opy_.bstack1ll111lll1l_opy_(target, strict)
        return bstack1lll11l1111_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll11l1111_opy_.bstack1ll111lll1l_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack1l1111111ll_opy_(self):
        return self.framework_name == bstack11l111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᔻ")
    def bstack11llllll1l1_opy_(self, target):
        return target if not self.bstack1l1111111ll_opy_() else self.bstack1l111111l11_opy_()
    @staticmethod
    def bstack1l111111l11_opy_():
        return str(os.getpid()) + str(threading.get_ident())