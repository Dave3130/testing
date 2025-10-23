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
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llll1ll111_opy_,
    bstack1lll111ll1l_opy_,
    bstack1lllll11l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llllll11ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11lll_opy_ import bstack1llll11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111111_opy_ import bstack1lll1l1111l_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
import weakref
class bstack1lll1l1l1ll_opy_(bstack1llllll111l_opy_):
    bstack1lll1lllll1_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack1lllll11l1l_opy_]]
    pages: Dict[str, Tuple[Callable, bstack1lllll11l1l_opy_]]
    def __init__(self, bstack1lll1lllll1_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1lll111l111_opy_ = dict()
        self.bstack1lll1lllll1_opy_ = bstack1lll1lllll1_opy_
        self.frameworks = frameworks
        bstack1llll11l1ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack111111l111_opy_, bstack1llll1ll111_opy_.POST), self.__1lll1111ll1_opy_)
        if any(bstack1llllll11ll_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1llllll11ll_opy_.bstack1111111l11_opy_(
                (bstack1llll1lllll_opy_.bstack11111111l1_opy_, bstack1llll1ll111_opy_.PRE), self.__1lll11111ll_opy_
            )
            bstack1llllll11ll_opy_.bstack1111111l11_opy_(
                (bstack1llll1lllll_opy_.QUIT, bstack1llll1ll111_opy_.POST), self.__1lll111111l_opy_
            )
    def __1lll1111ll1_opy_(
        self,
        f: bstack1llll11l1ll_opy_,
        bstack1lll11111l1_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack111111l_opy_ (u"ࠥࡲࡪࡽ࡟ࡱࡣࡪࡩࠧᆦ"):
                return
            contexts = bstack1lll11111l1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack111111l_opy_ (u"ࠦࡦࡨ࡯ࡶࡶ࠽ࡦࡱࡧ࡮࡬ࠤᆧ") in page.url:
                                self.logger.debug(bstack111111l_opy_ (u"࡙ࠧࡴࡰࡴ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡲࡪࡽࠠࡱࡣࡪࡩࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠢᆨ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll111ll1l_opy_.bstack1llll1lll1l_opy_(instance, self.bstack1lll1lllll1_opy_, True)
                                self.logger.debug(bstack111111l_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡵࡧࡧࡦࡡ࡬ࡲ࡮ࡺ࠺ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦᆩ") + str(instance.ref()) + bstack111111l_opy_ (u"ࠢࠣᆪ"))
        except Exception as e:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡶ࡮ࡴࡧࠡࡰࡨࡻࠥࡶࡡࡨࡧࠣ࠾ࠧᆫ"),e)
    def __1lll11111ll_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll111ll1l_opy_.get_state(instance, self.bstack1lll1lllll1_opy_, False):
            return
        if not f.bstack1lll111l11l_opy_(f.hub_url(driver)):
            self.bstack1lll111l111_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll111ll1l_opy_.bstack1llll1lll1l_opy_(instance, self.bstack1lll1lllll1_opy_, True)
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡢࡣࡴࡴ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡ࡬ࡲ࡮ࡺ࠺ࠡࡰࡲࡲࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᆬ") + str(instance.ref()) + bstack111111l_opy_ (u"ࠥࠦᆭ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll111ll1l_opy_.bstack1llll1lll1l_opy_(instance, self.bstack1lll1lllll1_opy_, True)
        self.logger.debug(bstack111111l_opy_ (u"ࠦࡤࡥ࡯࡯ࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࡣ࡮ࡴࡩࡵ࠼ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᆮ") + str(instance.ref()) + bstack111111l_opy_ (u"ࠧࠨᆯ"))
    def __1lll111111l_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1lll1111l1l_opy_(instance)
        self.logger.debug(bstack111111l_opy_ (u"ࠨ࡟ࡠࡱࡱࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡥࡱࡶ࡫ࡷ࠾ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᆰ") + str(instance.ref()) + bstack111111l_opy_ (u"ࠢࠣᆱ"))
    def bstack1llll111l11_opy_(self, context: bstack1lll1l1111l_opy_, reverse=True) -> List[Tuple[Callable, bstack1lllll11l1l_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1lll1111lll_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1llllll11ll_opy_.bstack1lll11lll1l_opy_(data[1])
                    and data[1].bstack1lll1111lll_opy_(context)
                    and getattr(data[0](), bstack111111l_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧᆲ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll111l1l1_opy_, reverse=reverse)
    def bstack1llll111111_opy_(self, context: bstack1lll1l1111l_opy_, reverse=True) -> List[Tuple[Callable, bstack1lllll11l1l_opy_]]:
        matches = []
        for data in self.bstack1lll111l111_opy_.values():
            if (
                data[1].bstack1lll1111lll_opy_(context)
                and getattr(data[0](), bstack111111l_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨᆳ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll111l1l1_opy_, reverse=reverse)
    def bstack1lll1111l11_opy_(self, instance: bstack1lllll11l1l_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1lll1111l1l_opy_(self, instance: bstack1lllll11l1l_opy_) -> bool:
        if self.bstack1lll1111l11_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll111ll1l_opy_.bstack1llll1lll1l_opy_(instance, self.bstack1lll1lllll1_opy_, False)
            return True
        return False