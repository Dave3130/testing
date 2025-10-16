# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
    bstack1lll111llll_opy_,
    bstack111111l111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1lllll1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll11l1_opy_ import bstack1llll11l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1llll11l111_opy_
from typing import Tuple, Dict, Any, List, Callable
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
import weakref
class bstack1lll1ll1111_opy_(bstack1llll1llll1_opy_):
    bstack1lll1l1l11l_opy_: str
    frameworks: List[str]
    drivers: Dict[str, Tuple[Callable, bstack111111l111_opy_]]
    pages: Dict[str, Tuple[Callable, bstack111111l111_opy_]]
    def __init__(self, bstack1lll1l1l11l_opy_: str, frameworks: List[str]):
        super().__init__()
        self.drivers = dict()
        self.pages = dict()
        self.bstack1lll1111ll1_opy_ = dict()
        self.bstack1lll1l1l11l_opy_ = bstack1lll1l1l11l_opy_
        self.frameworks = frameworks
        bstack1llll11l1l1_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1llllll1l1l_opy_, bstack1llllll1ll1_opy_.POST), self.__1lll1111l1l_opy_)
        if any(bstack1lllll1ll1l_opy_.NAME in f.lower().strip() for f in frameworks):
            bstack1lllll1ll1l_opy_.bstack1lllll1111l_opy_(
                (bstack1111111l11_opy_.bstack1111111ll1_opy_, bstack1llllll1ll1_opy_.PRE), self.__1lll111l111_opy_
            )
            bstack1lllll1ll1l_opy_.bstack1lllll1111l_opy_(
                (bstack1111111l11_opy_.QUIT, bstack1llllll1ll1_opy_.POST), self.__1lll111l1l1_opy_
            )
    def __1lll1111l1l_opy_(
        self,
        f: bstack1llll11l1l1_opy_,
        bstack1lll111111l_opy_: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if method_name != bstack1l_opy_ (u"ࠤࡱࡩࡼࡥࡰࡢࡩࡨࠦᆳ"):
                return
            contexts = bstack1lll111111l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                            if bstack1l_opy_ (u"ࠥࡥࡧࡵࡵࡵ࠼ࡥࡰࡦࡴ࡫ࠣᆴ") in page.url:
                                self.logger.debug(bstack1l_opy_ (u"ࠦࡘࡺ࡯ࡳ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡱࡩࡼࠦࡰࡢࡩࡨࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠨᆵ"))
                                self.pages[instance.ref()] = weakref.ref(page), instance
                                bstack1lll111llll_opy_.bstack1lllll11ll1_opy_(instance, self.bstack1lll1l1l11l_opy_, True)
                                self.logger.debug(bstack1l_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡴࡦ࡭ࡥࡠ࡫ࡱ࡭ࡹࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥᆶ") + str(instance.ref()) + bstack1l_opy_ (u"ࠨࠢᆷ"))
        except Exception as e:
            self.logger.debug(bstack1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡵ࡭ࡳ࡭ࠠ࡯ࡧࡺࠤࡵࡧࡧࡦࠢ࠽ࠦᆸ"),e)
    def __1lll111l111_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if instance.ref() in self.drivers or bstack1lll111llll_opy_.get_state(instance, self.bstack1lll1l1l11l_opy_, False):
            return
        if not f.bstack1lll1111lll_opy_(f.hub_url(driver)):
            self.bstack1lll1111ll1_opy_[instance.ref()] = weakref.ref(driver), instance
            bstack1lll111llll_opy_.bstack1lllll11ll1_opy_(instance, self.bstack1lll1l1l11l_opy_, True)
            self.logger.debug(bstack1l_opy_ (u"ࠣࡡࡢࡳࡳࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡠ࡫ࡱ࡭ࡹࡀࠠ࡯ࡱࡱࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᆹ") + str(instance.ref()) + bstack1l_opy_ (u"ࠤࠥᆺ"))
            return
        self.drivers[instance.ref()] = weakref.ref(driver), instance
        bstack1lll111llll_opy_.bstack1lllll11ll1_opy_(instance, self.bstack1lll1l1l11l_opy_, True)
        self.logger.debug(bstack1l_opy_ (u"ࠥࡣࡤࡵ࡮ࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࡢ࡭ࡳ࡯ࡴ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࠧᆻ") + str(instance.ref()) + bstack1l_opy_ (u"ࠦࠧᆼ"))
    def __1lll111l1l1_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, _ = exec
        if not instance.ref() in self.drivers:
            return
        self.bstack1lll1111l11_opy_(instance)
        self.logger.debug(bstack1l_opy_ (u"ࠧࡥ࡟ࡰࡰࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡷࡵࡪࡶ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᆽ") + str(instance.ref()) + bstack1l_opy_ (u"ࠨࠢᆾ"))
    def bstack1llll11llll_opy_(self, context: bstack1llll11l111_opy_, reverse=True) -> List[Tuple[Callable, bstack111111l111_opy_]]:
        matches = []
        if self.pages:
            for data in self.pages.values():
                if data[1].bstack1lll111l11l_opy_(context):
                    matches.append(data)
        if self.drivers:
            for data in self.drivers.values():
                if (
                    bstack1lllll1ll1l_opy_.bstack1lll11lll11_opy_(data[1])
                    and data[1].bstack1lll111l11l_opy_(context)
                    and getattr(data[0](), bstack1l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᆿ"), False)
                ):
                    matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll11111ll_opy_, reverse=reverse)
    def bstack1lll1ll1ll1_opy_(self, context: bstack1llll11l111_opy_, reverse=True) -> List[Tuple[Callable, bstack111111l111_opy_]]:
        matches = []
        for data in self.bstack1lll1111ll1_opy_.values():
            if (
                data[1].bstack1lll111l11l_opy_(context)
                and getattr(data[0](), bstack1l_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧᇀ"), False)
            ):
                matches.append(data)
        return sorted(matches, key=lambda d: d[1].bstack1lll11111ll_opy_, reverse=reverse)
    def bstack1lll11111l1_opy_(self, instance: bstack111111l111_opy_) -> bool:
        return instance and instance.ref() in self.drivers
    def bstack1lll1111l11_opy_(self, instance: bstack111111l111_opy_) -> bool:
        if self.bstack1lll11111l1_opy_(instance):
            self.drivers.pop(instance.ref())
            bstack1lll111llll_opy_.bstack1lllll11ll1_opy_(instance, self.bstack1lll1l1l11l_opy_, False)
            return True
        return False