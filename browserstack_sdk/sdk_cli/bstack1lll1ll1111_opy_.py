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
from browserstack_sdk.sdk_cli.bstack1lllll1llll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1lllll11l11_opy_,
    bstack1lll111lll1_opy_,
    bstack1llll1ll111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l111_opy_ import bstack1lll1ll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1llll1ll_opy_ import bstack1llll111l1l_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1lllll1llll_opy_ import bstack1lllll111l1_opy_
import weakref
class bstack1lll11l1lll_opy_(bstack1lllll111l1_opy_):
    bstack1lll1l1l11l_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1llll1ll111_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1llll1ll111_opy_]]
    def __init__(self, bstack1lll1l1l11l_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1ll1lll1l11_opy_ = dict()
        self.bstack1lll1l1l11l_opy_ = bstack1lll1l1l11l_opy_
        self.frameworks = frameworks
        bstack1lll1ll11ll_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.bstack1lllll11111_opy_, bstack1lllll11l11_opy_.POST), self.__1ll1llll11l_opy_)
        if any(bstack1lllllll1l1_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllllll1l1_opy_.bstack1lllll1l111_opy_(
                (bstack1llllll1111_opy_.bstack1lllllll11l_opy_, bstack1lllll11l11_opy_.PRE), self.__1ll1llll111_opy_
            )
            bstack1lllllll1l1_opy_.bstack1lllll1l111_opy_(
                (bstack1llllll1111_opy_.QUIT, bstack1lllll11l11_opy_.POST), self.__1ll1lll1ll1_opy_
            )
    def __1ll1llll11l_opy_(
        self,
        f: bstack1lll1ll11ll_opy_,
        bstack1ll1llllll1_opy_: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack1l111ll_opy_ (u"ࠣࡰࡨࡻࡤࡶࡡࡨࡧࠥᇎ"):
                return
            contexts = bstack1ll1llllll1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack1l111ll_opy_ (u"ࠤࡤࡦࡴࡻࡴ࠻ࡤ࡯ࡥࡳࡱࠢᇏ") in page.url:
                                self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡗࡹࡵࡲࡪࡰࡪࠤࡹ࡮ࡥࠡࡰࡨࡻࠥࡶࡡࡨࡧࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠧᇐ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll111lll1_opy_.bstack1lllll1ll1l_opy_(instance, self.bstack1lll1l1l11l_opy_, True)
                                self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡳࡥ࡬࡫࡟ࡪࡰ࡬ࡸ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࠤᇑ") + str(instance.ref()) + bstack1l111ll_opy_ (u"ࠧࠨᇒ"))
        except Exception as e:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦ࡮ࡦࡹࠣࡴࡦ࡭ࡥࠡ࠼ࠥᇓ"),e)
    def __1ll1llll111_opy_(
        self,
        f: bstack1lllllll1l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll111lll1_opy_.get_state(instance, self.bstack1lll1l1l11l_opy_, False):
            return
        if not f.bstack1ll1lll1l1l_opy_(f.hub_url(driver)):
            self.bstack1ll1lll1l11_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll111lll1_opy_.bstack1lllll1ll1l_opy_(instance, self.bstack1lll1l1l11l_opy_, True)
            self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡠࡡࡲࡲࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࡟ࡪࡰ࡬ࡸ࠿ࠦ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᇔ") + str(instance.ref()) + bstack1l111ll_opy_ (u"ࠣࠤᇕ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll111lll1_opy_.bstack1lllll1ll1l_opy_(instance, self.bstack1lll1l1l11l_opy_, True)
        self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡢࡣࡴࡴ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡ࡬ࡲ࡮ࡺ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᇖ") + str(instance.ref()) + bstack1l111ll_opy_ (u"ࠥࠦᇗ"))
    def __1ll1lll1ll1_opy_(
        self,
        f: bstack1lllllll1l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1ll1llll1l1_opy_(instance)
        self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࡣࡶࡻࡩࡵ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᇘ") + str(instance.ref()) + bstack1l111ll_opy_ (u"ࠧࠨᇙ"))
    def bstack1lll11lll11_opy_(self, context: bstack1llll111l1l_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1ll111_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1ll1lll1lll_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllllll1l1_opy_.bstack1lll1111l1l_opy_(data[1])
                    and data[1].bstack1ll1lll1lll_opy_(context)
                    and getattr(data[0](), bstack1l111ll_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᇚ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lllll11_opy_, reverse=reverse)
    def bstack1lll1lll1ll_opy_(self, context: bstack1llll111l1l_opy_, reverse=True) -> List[Tuple[Callable, bstack1llll1ll111_opy_]]:
        matches = []
        for data in self.bstack1ll1lll1l11_opy_.values():
            if (
                data[1].bstack1ll1lll1lll_opy_(context)
                and getattr(data[0](), bstack1l111ll_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᇛ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1ll1lllll11_opy_, reverse=reverse)
    def bstack1ll1lllll1l_opy_(self, instance: bstack1llll1ll111_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1ll1llll1l1_opy_(self, instance: bstack1llll1ll111_opy_) -> bool:
        if self.bstack1ll1lllll1l_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll111lll1_opy_.bstack1lllll1ll1l_opy_(instance, self.bstack1lll1l1l11l_opy_, False)
            return True
        return False