# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import (
    bstack1lllll11l1l_opy_,
    bstack1111111lll_opy_,
    bstack1lll11l1111_opy_,
    bstack1llllllll1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll11l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1lll1_opy_ import bstack1lll1l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1lll1l1ll1l_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1lll1l_opy_
import weakref
class bstack1lll1ll1l11_opy_(bstack1llll1lll1l_opy_):
    bstack1lll1ll1ll1_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llllllll1l_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llllllll1l_opy_]]
    def __init__(self, bstack1lll1ll1ll1_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1lll11111ll_opy_ = dict()
        self.bstack1lll1ll1ll1_opy_ = bstack1lll1ll1ll1_opy_
        self.frameworks = frameworks
        bstack1lll1l1ll11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1llll1ll11l_opy_, bstack1111111lll_opy_.POST), self.__1lll11111l1_opy_)
        if any(bstack1lllll11l11_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllll11l11_opy_.bstack1lllll1l11l_opy_(
                (bstack1lllll11l1l_opy_.bstack1111111111_opy_, bstack1111111lll_opy_.PRE), self.__1lll1111lll_opy_
            )
            bstack1lllll11l11_opy_.bstack1lllll1l11l_opy_(
                (bstack1lllll11l1l_opy_.QUIT, bstack1111111lll_opy_.POST), self.__1lll1111ll1_opy_
            )
    def __1lll11111l1_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1lll111l1l1_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack1ll1l_opy_ (u"ࠣࡰࡨࡻࡤࡶࡡࡨࡧࠥᆫ"):
                return
            contexts = bstack1lll111l1l1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack1ll1l_opy_ (u"ࠤࡤࡦࡴࡻࡴ࠻ࡤ࡯ࡥࡳࡱࠢᆬ") in page.url:
                                self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡗࡹࡵࡲࡪࡰࡪࠤࡹ࡮ࡥࠡࡰࡨࡻࠥࡶࡡࡨࡧࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠧᆭ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll11l1111_opy_.bstack1111111ll1_opy_(instance, self.bstack1lll1ll1ll1_opy_, True)
                                self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡳࡥ࡬࡫࡟ࡪࡰ࡬ࡸ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᆮ") + str(instance.ref()) + bstack1ll1l_opy_ (u"ࠧࠨᆯ"))
        except Exception as e:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦ࡮ࡦࡹࠣࡴࡦ࡭ࡥࠡ࠼ࠥᆰ"),e)
    def __1lll1111lll_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll11l1111_opy_.get_state(instance, self.bstack1lll1ll1ll1_opy_, False):
            return
        if not f.bstack1lll1111l11_opy_(f.hub_url(driver)):
            self.bstack1lll11111ll_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll11l1111_opy_.bstack1111111ll1_opy_(instance, self.bstack1lll1ll1ll1_opy_, True)
            self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡠࡡࡲࡲࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡪࡰ࡬ࡸ࠿ࠦ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᆱ") + str(instance.ref()) + bstack1ll1l_opy_ (u"ࠣࠤᆲ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll11l1111_opy_.bstack1111111ll1_opy_(instance, self.bstack1lll1ll1ll1_opy_, True)
        self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡢࡣࡴࡴ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡ࡬ࡲ࡮ࡺ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᆳ") + str(instance.ref()) + bstack1ll1l_opy_ (u"ࠥࠦᆴ"))
    def __1lll1111ll1_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1lll1111l1l_opy_(instance)
        self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࡣࡶࡻࡩࡵ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᆵ") + str(instance.ref()) + bstack1ll1l_opy_ (u"ࠧࠨᆶ"))
    def bstack1lll1lll1l1_opy_(self, context: bstack1lll1l1ll1l_opy_, reverse=True) -> List[Tuple[Callable, bstack1llllllll1l_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1lll1111111_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllll11l11_opy_.bstack1lll111ll1l_opy_(data[1])
                    and data[1].bstack1lll1111111_opy_(context)
                    and getattr(data[0](), bstack1ll1l_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᆷ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll111111l_opy_, reverse=reverse)
    def bstack1lll1l111l1_opy_(self, context: bstack1lll1l1ll1l_opy_, reverse=True) -> List[Tuple[Callable, bstack1llllllll1l_opy_]]:
        matches = []
        for data in self.bstack1lll11111ll_opy_.values():
            if (
                data[1].bstack1lll1111111_opy_(context)
                and getattr(data[0](), bstack1ll1l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᆸ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll111111l_opy_, reverse=reverse)
    def bstack1lll111l11l_opy_(self, instance: bstack1llllllll1l_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1lll1111l1l_opy_(self, instance: bstack1llllllll1l_opy_) -> bool:
        if self.bstack1lll111l11l_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll11l1111_opy_.bstack1111111ll1_opy_(instance, self.bstack1lll1ll1ll1_opy_, False)
            return True
        return False