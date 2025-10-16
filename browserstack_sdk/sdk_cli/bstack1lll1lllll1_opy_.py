# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1llllllll11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack11111111ll_opy_,
    bstack1lllllll1ll_opy_,
    bstack1lll11ll111_opy_,
    bstack1llllll11ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack111111111l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1lll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1lll1l11l11_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1llllllll11_opy_
import weakref
class bstack1llll111ll1_opy_(bstack1llllllll11_opy_):
    bstack1lll1l111l1_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llllll11ll_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llllll11ll_opy_]]
    def __init__(self, bstack1lll1l111l1_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1lll111111l_opy_ = dict()
        self.bstack1lll1l111l1_opy_ = bstack1lll1l111l1_opy_
        self.frameworks = frameworks
        bstack1lll1lll1l1_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.bstack1llll1lllll_opy_, bstack1lllllll1ll_opy_.POST), self.__1lll111l1ll_opy_)
        if any(bstack111111111l_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack111111111l_opy_.bstack1llllll1l1l_opy_(
                (bstack11111111ll_opy_.bstack1llll1l1ll1_opy_, bstack1lllllll1ll_opy_.PRE), self.__1lll1111ll1_opy_
            )
            bstack111111111l_opy_.bstack1llllll1l1l_opy_(
                (bstack11111111ll_opy_.QUIT, bstack1lllllll1ll_opy_.POST), self.__1lll1111l1l_opy_
            )
    def __1lll111l1ll_opy_(
        self,
        f: bstack1lll1lll1l1_opy_,
        bstack1lll1111l11_opy_: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack1ll1ll1_opy_ (u"ࠣࡰࡨࡻࡤࡶࡡࡨࡧࠥᆲ"):
                return
            contexts = bstack1lll1111l11_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack1ll1ll1_opy_ (u"ࠤࡤࡦࡴࡻࡴ࠻ࡤ࡯ࡥࡳࡱࠢᆳ") in page.url:
                                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡗࡹࡵࡲࡪࡰࡪࠤࡹ࡮ࡥࠡࡰࡨࡻࠥࡶࡡࡨࡧࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠧᆴ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll11ll111_opy_.bstack1lllll1l1ll_opy_(instance, self.bstack1lll1l111l1_opy_, True)
                                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡳࡥ࡬࡫࡟ࡪࡰ࡬ࡸ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᆵ") + str(instance.ref()) + bstack1ll1ll1_opy_ (u"ࠧࠨᆶ"))
        except Exception as e:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦ࡮ࡦࡹࠣࡴࡦ࡭ࡥࠡ࠼ࠥᆷ"),e)
    def __1lll1111ll1_opy_(
        self,
        f: bstack111111111l_opy_,
        driver: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll11ll111_opy_.get_state(instance, self.bstack1lll1l111l1_opy_, False):
            return
        if not f.bstack1lll111l11l_opy_(f.hub_url(driver)):
            self.bstack1lll111111l_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll11ll111_opy_.bstack1lllll1l1ll_opy_(instance, self.bstack1lll1l111l1_opy_, True)
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡠࡡࡲࡲࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡪࡰ࡬ࡸ࠿ࠦ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᆸ") + str(instance.ref()) + bstack1ll1ll1_opy_ (u"ࠣࠤᆹ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll11ll111_opy_.bstack1lllll1l1ll_opy_(instance, self.bstack1lll1l111l1_opy_, True)
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡢࡣࡴࡴ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡ࡬ࡲ࡮ࡺ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᆺ") + str(instance.ref()) + bstack1ll1ll1_opy_ (u"ࠥࠦᆻ"))
    def __1lll1111l1l_opy_(
        self,
        f: bstack111111111l_opy_,
        driver: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1lll1111lll_opy_(instance)
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࡣࡶࡻࡩࡵ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᆼ") + str(instance.ref()) + bstack1ll1ll1_opy_ (u"ࠧࠨᆽ"))
    def bstack1lll1l1l11l_opy_(self, context: bstack1lll1l11l11_opy_, reverse=True) -> List[Tuple[Callable, bstack1llllll11ll_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1lll111l1l1_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack111111111l_opy_.bstack1lll11ll1l1_opy_(data[1])
                    and data[1].bstack1lll111l1l1_opy_(context)
                    and getattr(data[0](), bstack1ll1ll1_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᆾ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll11111ll_opy_, reverse=reverse)
    def bstack1lll1ll11ll_opy_(self, context: bstack1lll1l11l11_opy_, reverse=True) -> List[Tuple[Callable, bstack1llllll11ll_opy_]]:
        matches = []
        for data in self.bstack1lll111111l_opy_.values():
            if (
                data[1].bstack1lll111l1l1_opy_(context)
                and getattr(data[0](), bstack1ll1ll1_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᆿ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll11111ll_opy_, reverse=reverse)
    def bstack1lll11111l1_opy_(self, instance: bstack1llllll11ll_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1lll1111lll_opy_(self, instance: bstack1llllll11ll_opy_) -> bool:
        if self.bstack1lll11111l1_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll11ll111_opy_.bstack1lllll1l1ll_opy_(instance, self.bstack1lll1l111l1_opy_, False)
            return True
        return False