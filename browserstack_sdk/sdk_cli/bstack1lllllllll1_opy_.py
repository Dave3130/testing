# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import logging
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1lll1111111_opy_ import bstack1ll1lll1111_opy_, bstack1lll1l1111l_opy_
import os
import threading
class bstack1llll1ll111_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack111111l_opy_ (u"ࠥࡌࡴࡵ࡫ࡔࡶࡤࡸࡪ࠴ࡻࡾࠤᓼ").format(self.name)
class bstack1llll1lllll_opy_(Enum):
    NONE = 0
    bstack111111l111_opy_ = 1
    bstack1ll1llll11l_opy_ = 3
    bstack11111111l1_opy_ = 4
    bstack1l11111l1l1_opy_ = 5
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
        return bstack111111l_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡺࡥ࠯ࡽࢀࠦᓽ").format(self.name)
class bstack1lllll11l1l_opy_(bstack1ll1lll1111_opy_):
    framework_name: str
    framework_version: str
    state: bstack1llll1lllll_opy_
    previous_state: bstack1llll1lllll_opy_
    bstack1lll111l1l1_opy_: datetime
    bstack1l1111l11ll_opy_: datetime
    def __init__(
        self,
        context: bstack1lll1l1111l_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1llll1lllll_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1llll1lllll_opy_.NONE
        self.bstack1lll111l1l1_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1llll1lll1l_opy_(self, bstack1l1111l11l1_opy_: bstack1llll1lllll_opy_):
        bstack1l1111l1111_opy_ = bstack1llll1lllll_opy_(bstack1l1111l11l1_opy_).name
        if not bstack1l1111l1111_opy_:
            return False
        if bstack1l1111l11l1_opy_ == self.state:
            return False
        if self.state == bstack1llll1lllll_opy_.bstack1ll1llll11l_opy_: # bstack1l11111l11l_opy_ bstack1l1111111ll_opy_ for bstack1l11111l1ll_opy_ in Playwright, it bstack1l11111llll_opy_ bstack1l11111111l_opy_ multiple times bstack1l111111l1l_opy_ a new state
            return True
        if (
            bstack1l1111l11l1_opy_ == bstack1llll1lllll_opy_.NONE
            or (self.state != bstack1llll1lllll_opy_.NONE and bstack1l1111l11l1_opy_ == bstack1llll1lllll_opy_.bstack111111l111_opy_)
            or (self.state < bstack1llll1lllll_opy_.bstack111111l111_opy_ and bstack1l1111l11l1_opy_ == bstack1llll1lllll_opy_.bstack11111111l1_opy_)
            or (self.state < bstack1llll1lllll_opy_.bstack111111l111_opy_ and bstack1l1111l11l1_opy_ == bstack1llll1lllll_opy_.QUIT)
        ):
            raise ValueError(bstack111111l_opy_ (u"ࠧ࡯࡮ࡷࡣ࡯࡭ࡩࠦࡳࡵࡣࡷࡩࠥࡺࡲࡢࡰࡶ࡭ࡹ࡯࡯࡯࠼ࠣࠦᓾ") + str(self.state) + bstack111111l_opy_ (u"ࠨࠠ࠾ࡀࠣࠦᓿ") + str(bstack1l1111l11l1_opy_))
        self.previous_state = self.state
        self.state = bstack1l1111l11l1_opy_
        self.bstack1l1111l11ll_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack1lll111ll1l_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llll111l1l_opy_: Dict[str, bstack1lllll11l1l_opy_] = dict()
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
    def bstack1l1lll11l11_opy_(self, instance: bstack1lllll11l1l_opy_, method_name: str, bstack1l1lll1111l_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1l1ll1llll1_opy_(
        self, method_name, previous_state: bstack1llll1lllll_opy_, *args, **kwargs
    ) -> bstack1llll1lllll_opy_:
        return
    @abc.abstractmethod
    def bstack1l1llll111l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1l1lll1l111_opy_(self, bstack1l111111l11_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack1l111111l11_opy_:
                bstack1l11111ll1l_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1l11111ll1l_opy_):
                    self.logger.warning(bstack111111l_opy_ (u"ࠢࡶࡰࡳࡥࡹࡩࡨࡦࡦࠣࡱࡪࡺࡨࡰࡦ࠽ࠤࠧᔀ") + str(method_name) + bstack111111l_opy_ (u"ࠣࠤᔁ"))
                    continue
                bstack1l1lll11111_opy_ = self.bstack1l1ll1llll1_opy_(
                    method_name, previous_state=bstack1llll1lllll_opy_.NONE
                )
                bstack1l11111lll1_opy_ = self.bstack1l11111l111_opy_(
                    method_name,
                    (bstack1l1lll11111_opy_ if bstack1l1lll11111_opy_ else bstack1llll1lllll_opy_.NONE),
                    bstack1l11111ll1l_opy_,
                )
                if not callable(bstack1l11111lll1_opy_):
                    self.logger.warning(bstack111111l_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠢࡱࡳࡹࠦࡰࡢࡶࡦ࡬ࡪࡪ࠺ࠡࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࠪࡾࡷࡪࡲࡦ࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࡿ࠽ࠤࠧᔂ") + str(self.framework_version) + bstack111111l_opy_ (u"ࠥ࠭ࠧᔃ"))
                    continue
                setattr(clazz, method_name, bstack1l11111lll1_opy_)
    def bstack1l11111l111_opy_(
        self,
        method_name: str,
        bstack1l1lll11111_opy_: bstack1llll1lllll_opy_,
        bstack1l11111ll1l_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack1111ll111_opy_ = datetime.now()
            (bstack1l1lll11111_opy_,) = wrapped.__vars__
            bstack1l1lll11111_opy_ = (
                bstack1l1lll11111_opy_
                if bstack1l1lll11111_opy_ and bstack1l1lll11111_opy_ != bstack1llll1lllll_opy_.NONE
                else self.bstack1l1ll1llll1_opy_(method_name, previous_state=bstack1l1lll11111_opy_, *args, **kwargs)
            )
            if bstack1l1lll11111_opy_ == bstack1llll1lllll_opy_.bstack111111l111_opy_:
                ctx = bstack1ll1lll1111_opy_.create_context(self.bstack1l111111ll1_opy_(target))
                if not self.bstack1l11111ll11_opy_() or ctx.id not in bstack1lll111ll1l_opy_.bstack1llll111l1l_opy_:
                    bstack1lll111ll1l_opy_.bstack1llll111l1l_opy_[ctx.id] = bstack1lllll11l1l_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1l1lll11111_opy_
                    )
                self.logger.debug(bstack111111l_opy_ (u"ࠦࡼࡸࡡࡱࡲࡨࡨࠥࡳࡥࡵࡪࡲࡨࠥࡩࡲࡦࡣࡷࡩࡩࡀࠠࡼࡶࡤࡶ࡬࡫ࡴ࠯ࡡࡢࡧࡱࡧࡳࡴࡡࡢࢁࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡦࡸࡽࡃࡻࡤࡶࡻ࠲࡮ࡪࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧᔄ") + str(bstack1lll111ll1l_opy_.bstack1llll111l1l_opy_.keys()) + bstack111111l_opy_ (u"ࠧࠨᔅ"))
            else:
                self.logger.debug(bstack111111l_opy_ (u"ࠨࡷࡳࡣࡳࡴࡪࡪࠠ࡮ࡧࡷ࡬ࡴࡪࠠࡪࡰࡹࡳࡰ࡫ࡤ࠻ࠢࡾࡸࡦࡸࡧࡦࡶ࠱ࡣࡤࡩ࡬ࡢࡵࡶࡣࡤࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡹ࠽ࠣᔆ") + str(bstack1lll111ll1l_opy_.bstack1llll111l1l_opy_.keys()) + bstack111111l_opy_ (u"ࠢࠣᔇ"))
            instance = bstack1lll111ll1l_opy_.bstack1ll11ll1lll_opy_(self.bstack1l111111ll1_opy_(target))
            if bstack1l1lll11111_opy_ == bstack1llll1lllll_opy_.NONE or not instance:
                ctx = bstack1ll1lll1111_opy_.create_context(self.bstack1l111111ll1_opy_(target))
                self.logger.warning(bstack111111l_opy_ (u"ࠣࡹࡵࡥࡵࡶࡥࡥࠢࡰࡩࡹ࡮࡯ࡥࠢࡸࡲࡹࡸࡡࡤ࡭ࡨࡨ࠿ࠦࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁࠥࡩࡴࡹ࠿ࡾࡧࡹࡾࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧᔈ") + str(bstack1lll111ll1l_opy_.bstack1llll111l1l_opy_.keys()) + bstack111111l_opy_ (u"ࠤࠥᔉ"))
                return bstack1l11111ll1l_opy_(target, *args, **kwargs)
            bstack1l1ll1l1l11_opy_ = self.bstack1l1llll111l_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll11111_opy_, bstack1llll1ll111_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1llll1lll1l_opy_(bstack1l1lll11111_opy_):
                self.logger.debug(bstack111111l_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡧࡧࠤࡸࡺࡡࡵࡧ࠰ࡸࡷࡧ࡮ࡴ࡫ࡷ࡭ࡴࡴ࠺ࠡࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡵࡸࡥࡷ࡫ࡲࡹࡸࡥࡳࡵࡣࡷࡩࢂࠦ࠽࠿ࠢࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡹࡴࡢࡶࡨࢁࠥ࠮ࡻࡵࡻࡳࡩ࠭ࡺࡡࡳࡩࡨࡸ࠮ࢃ࠮ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡼࡣࡵ࡫ࡸࢃࠩࠡ࡝ࠥᔊ") + str(instance.ref()) + bstack111111l_opy_ (u"ࠦࡢࠨᔋ"))
            result = (
                bstack1l1ll1l1l11_opy_(target, bstack1l11111ll1l_opy_, *args, **kwargs)
                if callable(bstack1l1ll1l1l11_opy_)
                else bstack1l11111ll1l_opy_(target, *args, **kwargs)
            )
            bstack1l1111111l1_opy_ = self.bstack1l1llll111l_opy_(
                target,
                (instance, method_name),
                (bstack1l1lll11111_opy_, bstack1llll1ll111_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1l1lll11l11_opy_(instance, method_name, datetime.now() - bstack1111ll111_opy_, *args, **kwargs)
            return bstack1l1111111l1_opy_ if bstack1l1111111l1_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1l1lll11111_opy_,)
        return wrapped
    @staticmethod
    def bstack1ll11ll1lll_opy_(target: object, strict=True):
        ctx = bstack1ll1lll1111_opy_.create_context(target)
        instance = bstack1lll111ll1l_opy_.bstack1llll111l1l_opy_.get(ctx.id, None)
        if instance and instance.bstack1ll1ll1llll_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l11l1111l1_opy_(
        ctx: bstack1lll1l1111l_opy_, state: bstack1llll1lllll_opy_, reverse=True
    ) -> List[bstack1lllll11l1l_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack1lll111ll1l_opy_.bstack1llll111l1l_opy_.values(),
            ),
            key=lambda t: t.bstack1lll111l1l1_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllllll11l_opy_(instance: bstack1lllll11l1l_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def get_state(instance: bstack1lllll11l1l_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1llll1lll1l_opy_(instance: bstack1lllll11l1l_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack1lll111ll1l_opy_.logger.debug(bstack111111l_opy_ (u"ࠧࡹࡥࡵࡡࡶࡸࡦࡺࡥ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࡳࡧࡩࠬ࠮ࢃࠠ࡬ࡧࡼࡁࢀࡱࡥࡺࡿࠣࡺࡦࡲࡵࡦ࠿ࠥᔌ") + str(value) + bstack111111l_opy_ (u"ࠨࠢᔍ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack1lll111ll1l_opy_.bstack1ll11ll1lll_opy_(target, strict)
        return bstack1lll111ll1l_opy_.get_state(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack1lll111ll1l_opy_.bstack1ll11ll1lll_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack1l11111ll11_opy_(self):
        return self.framework_name == bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᔎ")
    def bstack1l111111ll1_opy_(self, target):
        return target if not self.bstack1l11111ll11_opy_() else self.bstack1l111111lll_opy_()
    @staticmethod
    def bstack1l111111lll_opy_():
        return str(os.getpid()) + str(threading.get_ident())