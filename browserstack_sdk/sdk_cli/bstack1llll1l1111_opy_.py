# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import (
    bstack1lll111lll1_opy_,
    bstack1lllllll11l_opy_,
    bstack1111111111_opy_,
    bstack1llll1lllll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
from bstack_utils.constants import EVENTS
class bstack1llllll1ll1_opy_(bstack1lll111lll1_opy_):
    bstack1l1ll1lll11_opy_ = bstack1lll11l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣᕕ")
    NAME = bstack1lll11l_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᕖ")
    bstack1llll111lll_opy_ = bstack1lll11l_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࠦᕗ")
    bstack1llll111l1l_opy_ = bstack1lll11l_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᕘ")
    bstack11llll11ll1_opy_ = bstack1lll11l_opy_ (u"ࠧ࡯࡮ࡱࡷࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᕙ")
    bstack1lll1llll1l_opy_ = bstack1lll11l_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᕚ")
    bstack1lll11111ll_opy_ = bstack1lll11l_opy_ (u"ࠢࡪࡵࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡫ࡹࡧࠨᕛ")
    bstack11llll11111_opy_ = bstack1lll11l_opy_ (u"ࠣࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᕜ")
    bstack11llll11lll_opy_ = bstack1lll11l_opy_ (u"ࠤࡨࡲࡩ࡫ࡤࡠࡣࡷࠦᕝ")
    bstack1lllllllll1_opy_ = bstack1lll11l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠦᕞ")
    bstack1llllll1l11_opy_ = bstack1lll11l_opy_ (u"ࠦࡳ࡫ࡷࡴࡧࡶࡷ࡮ࡵ࡮ࠣᕟ")
    bstack11llll111l1_opy_ = bstack1lll11l_opy_ (u"ࠧ࡭ࡥࡵࠤᕠ")
    bstack1l11l11111l_opy_ = bstack1lll11l_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᕡ")
    bstack1l1lll11l1l_opy_ = bstack1lll11l_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࠥᕢ")
    bstack1l1ll1l1lll_opy_ = bstack1lll11l_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࡥࡸࡿ࡮ࡤࠤᕣ")
    bstack11llll11l1l_opy_ = bstack1lll11l_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᕤ")
    bstack1l1111111l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1llll11llll_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1l1l11_opy_: Any
    bstack1l1ll1l1ll1_opy_: Dict
    def __init__(
        self,
        bstack1llll11llll_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1llll1l1l11_opy_: Dict[str, Any],
        methods=[bstack1lll11l_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧᕥ"), bstack1lll11l_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࠦᕦ"), bstack1lll11l_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࠨᕧ"), bstack1lll11l_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᕨ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1llll11llll_opy_ = bstack1llll11llll_opy_
        self.platform_index = platform_index
        self.bstack1l1lll11ll1_opy_(methods)
        self.bstack1llll1l1l11_opy_ = bstack1llll1l1l11_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll111lll1_opy_.get_data(bstack1llllll1ll1_opy_.bstack1llll111l1l_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll111lll1_opy_.get_data(bstack1llllll1ll1_opy_.bstack1llll111lll_opy_, target, strict)
    @staticmethod
    def bstack11llll111ll_opy_(target: object, strict=True):
        return bstack1lll111lll1_opy_.get_data(bstack1llllll1ll1_opy_.bstack11llll11ll1_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll111lll1_opy_.get_data(bstack1llllll1ll1_opy_.bstack1lll1llll1l_opy_, target, strict)
    @staticmethod
    def bstack1lll1111ll1_opy_(instance: bstack1lllllll11l_opy_) -> bool:
        return bstack1lll111lll1_opy_.get_state(instance, bstack1llllll1ll1_opy_.bstack1lll11111ll_opy_, False)
    @staticmethod
    def bstack1l1lll11l11_opy_(instance: bstack1lllllll11l_opy_, default_value=None):
        return bstack1lll111lll1_opy_.get_state(instance, bstack1llllll1ll1_opy_.bstack1llll111lll_opy_, default_value)
    @staticmethod
    def bstack1l1ll1lll1l_opy_(instance: bstack1lllllll11l_opy_, default_value=None):
        return bstack1lll111lll1_opy_.get_state(instance, bstack1llllll1ll1_opy_.bstack1lll1llll1l_opy_, default_value)
    @staticmethod
    def bstack1ll1lllll1l_opy_(hub_url: str, bstack11llll1l111_opy_=bstack1lll11l_opy_ (u"ࠢ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠦᕩ")):
        try:
            bstack11llll11l11_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll11l11_opy_.endswith(bstack11llll1l111_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll1111l_opy_(method_name: str):
        return method_name == bstack1lll11l_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᕪ")
    @staticmethod
    def bstack1llllllllll_opy_(method_name: str, *args):
        return (
            bstack1llllll1ll1_opy_.bstack1l1lll1111l_opy_(method_name)
            and bstack1llllll1ll1_opy_.bstack1lllll1111l_opy_(*args) == bstack1llllll1ll1_opy_.bstack1llllll1l11_opy_
        )
    @staticmethod
    def bstack1l1lll111ll_opy_(method_name: str, *args):
        if not bstack1llllll1ll1_opy_.bstack1l1lll1111l_opy_(method_name):
            return False
        if not bstack1llllll1ll1_opy_.bstack1l1lll11l1l_opy_ in bstack1llllll1ll1_opy_.bstack1lllll1111l_opy_(*args):
            return False
        bstack1l1ll1l1l11_opy_ = bstack1llllll1ll1_opy_.bstack1l1lll1l111_opy_(*args)
        return bstack1l1ll1l1l11_opy_ and bstack1lll11l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᕫ") in bstack1l1ll1l1l11_opy_ and bstack1lll11l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕬ") in bstack1l1ll1l1l11_opy_[bstack1lll11l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᕭ")]
    @staticmethod
    def bstack1l1ll1ll11l_opy_(method_name: str, *args):
        if not bstack1llllll1ll1_opy_.bstack1l1lll1111l_opy_(method_name):
            return False
        if not bstack1llllll1ll1_opy_.bstack1l1lll11l1l_opy_ in bstack1llllll1ll1_opy_.bstack1lllll1111l_opy_(*args):
            return False
        bstack1l1ll1l1l11_opy_ = bstack1llllll1ll1_opy_.bstack1l1lll1l111_opy_(*args)
        return (
            bstack1l1ll1l1l11_opy_
            and bstack1lll11l_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᕮ") in bstack1l1ll1l1l11_opy_
            and bstack1lll11l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡧࡷ࡯ࡰࡵࠤᕯ") in bstack1l1ll1l1l11_opy_[bstack1lll11l_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᕰ")]
        )
    @staticmethod
    def bstack1lllll1111l_opy_(*args):
        return str(bstack1llllll1ll1_opy_.bstack1l1ll1ll1l1_opy_(*args)).lower()
    @staticmethod
    def bstack1l1ll1ll1l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll1l111_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack11l11lll1l_opy_(driver):
        command_executor = getattr(driver, bstack1lll11l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕱ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1lll11l_opy_ (u"ࠤࡢࡹࡷࡲࠢᕲ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1lll11l_opy_ (u"ࠥࡣࡨࡲࡩࡦࡰࡷࡣࡨࡵ࡮ࡧ࡫ࡪࠦᕳ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1lll11l_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡣࡸ࡫ࡲࡷࡧࡵࡣࡦࡪࡤࡳࠤᕴ"), None)
        return hub_url
    def bstack1llll1l111l_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1lll11l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᕵ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1lll11l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕶ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1lll11l_opy_ (u"ࠢࡠࡷࡵࡰࠧᕷ")):
                setattr(command_executor, bstack1lll11l_opy_ (u"ࠣࡡࡸࡶࡱࠨᕸ"), hub_url)
                result = True
        if result:
            self.bstack1llll11llll_opy_ = hub_url
            bstack1llllll1ll1_opy_.bstack1llll1ll11l_opy_(instance, bstack1llllll1ll1_opy_.bstack1llll111lll_opy_, hub_url)
            bstack1llllll1ll1_opy_.bstack1llll1ll11l_opy_(
                instance, bstack1llllll1ll1_opy_.bstack1lll11111ll_opy_, bstack1llllll1ll1_opy_.bstack1ll1lllll1l_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1ll1l1l1l_opy_(bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_]):
        return bstack1lll11l_opy_ (u"ࠤ࠽ࠦᕹ").join((bstack1111111111_opy_(bstack1lllll1l111_opy_[0]).name, bstack1llll1lllll_opy_(bstack1lllll1l111_opy_[1]).name))
    @staticmethod
    def bstack1lllll11111_opy_(bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_], callback: Callable):
        bstack1l1lll11lll_opy_ = bstack1llllll1ll1_opy_.bstack1l1ll1l1l1l_opy_(bstack1lllll1l111_opy_)
        if not bstack1l1lll11lll_opy_ in bstack1llllll1ll1_opy_.bstack1l1111111l1_opy_:
            bstack1llllll1ll1_opy_.bstack1l1111111l1_opy_[bstack1l1lll11lll_opy_] = []
        bstack1llllll1ll1_opy_.bstack1l1111111l1_opy_[bstack1l1lll11lll_opy_].append(callback)
    def bstack1l1ll1ll1ll_opy_(self, instance: bstack1lllllll11l_opy_, method_name: str, bstack1l1ll1l11ll_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1lll11l_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࠥᕺ")):
            return
        cmd = args[0] if method_name == bstack1lll11l_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᕻ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll1111l_opy_ = bstack1lll11l_opy_ (u"ࠧࡀࠢᕼ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠢᕽ") + bstack11llll1111l_opy_, bstack1l1ll1l11ll_opy_)
    def bstack1l1lll1l11l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll11111_opy_, bstack1l1lll1l1l1_opy_ = bstack1lllll1l111_opy_
        bstack1l1lll11lll_opy_ = bstack1llllll1ll1_opy_.bstack1l1ll1l1l1l_opy_(bstack1lllll1l111_opy_)
        self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡰࡰࡢ࡬ࡴࡵ࡫࠻ࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᕾ") + str(kwargs) + bstack1lll11l_opy_ (u"ࠣࠤᕿ"))
        if bstack1l1lll11111_opy_ == bstack1111111111_opy_.QUIT:
            if bstack1l1lll1l1l1_opy_ == bstack1llll1lllll_opy_.PRE:
                bstack1ll111111l1_opy_ = bstack1llll1l1l1l_opy_.bstack1ll111l1ll1_opy_(EVENTS.bstack11ll111ll_opy_.value)
                bstack1lll111lll1_opy_.bstack1llll1ll11l_opy_(instance, EVENTS.bstack11ll111ll_opy_.value, bstack1ll111111l1_opy_)
                self.logger.debug(bstack1lll11l_opy_ (u"ࠤ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࢁࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠦࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠨᖀ").format(instance, method_name, bstack1l1lll11111_opy_, bstack1l1lll1l1l1_opy_))
        if bstack1l1lll11111_opy_ == bstack1111111111_opy_.bstack1llll1l1ll1_opy_:
            if bstack1l1lll1l1l1_opy_ == bstack1llll1lllll_opy_.POST and not bstack1llllll1ll1_opy_.bstack1llll111l1l_opy_ in instance.data:
                session_id = getattr(target, bstack1lll11l_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᖁ"), None)
                if session_id:
                    instance.data[bstack1llllll1ll1_opy_.bstack1llll111l1l_opy_] = session_id
        elif (
            bstack1l1lll11111_opy_ == bstack1111111111_opy_.bstack1llll1ll111_opy_
            and bstack1llllll1ll1_opy_.bstack1lllll1111l_opy_(*args) == bstack1llllll1ll1_opy_.bstack1llllll1l11_opy_
        ):
            if bstack1l1lll1l1l1_opy_ == bstack1llll1lllll_opy_.PRE:
                hub_url = bstack1llllll1ll1_opy_.bstack11l11lll1l_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1llllll1ll1_opy_.bstack1llll111lll_opy_: hub_url,
                            bstack1llllll1ll1_opy_.bstack1lll11111ll_opy_: bstack1llllll1ll1_opy_.bstack1ll1lllll1l_opy_(hub_url),
                            bstack1llllll1ll1_opy_.bstack1lllllllll1_opy_: int(
                                os.environ.get(bstack1lll11l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᖂ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1ll1l1l11_opy_ = bstack1llllll1ll1_opy_.bstack1l1lll1l111_opy_(*args)
                bstack11llll111ll_opy_ = bstack1l1ll1l1l11_opy_.get(bstack1lll11l_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᖃ"), None) if bstack1l1ll1l1l11_opy_ else None
                if isinstance(bstack11llll111ll_opy_, dict):
                    instance.data[bstack1llllll1ll1_opy_.bstack11llll11ll1_opy_] = copy.deepcopy(bstack11llll111ll_opy_)
                    instance.data[bstack1llllll1ll1_opy_.bstack1lll1llll1l_opy_] = bstack11llll111ll_opy_
            elif bstack1l1lll1l1l1_opy_ == bstack1llll1lllll_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1lll11l_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧᖄ"), dict()).get(bstack1lll11l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡊࡦࠥᖅ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1llllll1ll1_opy_.bstack1llll111l1l_opy_: framework_session_id,
                                bstack1llllll1ll1_opy_.bstack11llll11111_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1lll11111_opy_ == bstack1111111111_opy_.bstack1llll1ll111_opy_
            and bstack1llllll1ll1_opy_.bstack1lllll1111l_opy_(*args) == bstack1llllll1ll1_opy_.bstack11llll11l1l_opy_
            and bstack1l1lll1l1l1_opy_ == bstack1llll1lllll_opy_.POST
        ):
            instance.data[bstack1llllll1ll1_opy_.bstack11llll11lll_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1lll11lll_opy_ in bstack1llllll1ll1_opy_.bstack1l1111111l1_opy_:
            bstack1l1ll1ll111_opy_ = None
            for callback in bstack1llllll1ll1_opy_.bstack1l1111111l1_opy_[bstack1l1lll11lll_opy_]:
                try:
                    bstack1l1ll1llll1_opy_ = callback(self, target, exec, bstack1lllll1l111_opy_, result, *args, **kwargs)
                    if bstack1l1ll1ll111_opy_ == None:
                        bstack1l1ll1ll111_opy_ = bstack1l1ll1llll1_opy_
                except Exception as e:
                    self.logger.error(bstack1lll11l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࠨᖆ") + str(e) + bstack1lll11l_opy_ (u"ࠤࠥᖇ"))
                    traceback.print_exc()
            if bstack1l1lll11111_opy_ == bstack1111111111_opy_.QUIT:
                if bstack1l1lll1l1l1_opy_ == bstack1llll1lllll_opy_.POST:
                    bstack1ll111111l1_opy_ = bstack1lll111lll1_opy_.get_state(instance, EVENTS.bstack11ll111ll_opy_.value)
                    if bstack1ll111111l1_opy_!=None:
                        bstack1llll1l1l1l_opy_.end(EVENTS.bstack11ll111ll_opy_.value, bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᖈ"), bstack1ll111111l1_opy_+bstack1lll11l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᖉ"), True, None)
            if bstack1l1lll1l1l1_opy_ == bstack1llll1lllll_opy_.PRE and callable(bstack1l1ll1ll111_opy_):
                return bstack1l1ll1ll111_opy_
            elif bstack1l1lll1l1l1_opy_ == bstack1llll1lllll_opy_.POST and bstack1l1ll1ll111_opy_:
                return bstack1l1ll1ll111_opy_
    def bstack1l1ll1lllll_opy_(
        self, method_name, previous_state: bstack1111111111_opy_, *args, **kwargs
    ) -> bstack1111111111_opy_:
        if method_name == bstack1lll11l_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢᖊ") or method_name == bstack1lll11l_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᖋ"):
            return bstack1111111111_opy_.bstack1llll1l1ll1_opy_
        if method_name == bstack1lll11l_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᖌ"):
            return bstack1111111111_opy_.QUIT
        if method_name == bstack1lll11l_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᖍ"):
            if previous_state != bstack1111111111_opy_.NONE:
                command_name = bstack1llllll1ll1_opy_.bstack1lllll1111l_opy_(*args)
                if command_name == bstack1llllll1ll1_opy_.bstack1llllll1l11_opy_:
                    return bstack1111111111_opy_.bstack1llll1l1ll1_opy_
            return bstack1111111111_opy_.bstack1llll1ll111_opy_
        return bstack1111111111_opy_.NONE