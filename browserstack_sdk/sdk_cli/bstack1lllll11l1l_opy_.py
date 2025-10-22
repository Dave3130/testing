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
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llll1ll1l1_opy_ import (
    bstack1lll111l1l1_opy_,
    bstack1lllllll1l1_opy_,
    bstack1llll1lll1l_opy_,
    bstack1lllll1l1ll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack1l11l1l11_opy_ import bstack1llllll11ll_opy_
from bstack_utils.constants import EVENTS
class bstack1lllll11111_opy_(bstack1lll111l1l1_opy_):
    bstack1l1ll1lll11_opy_ = bstack111l1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣᕎ")
    NAME = bstack111l1l_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᕏ")
    bstack1lll1l11lll_opy_ = bstack111l1l_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࠦᕐ")
    bstack1lll1l11l1l_opy_ = bstack111l1l_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᕑ")
    bstack11llll11ll1_opy_ = bstack111l1l_opy_ (u"ࠧ࡯࡮ࡱࡷࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᕒ")
    bstack1lll1l1l11l_opy_ = bstack111l1l_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᕓ")
    bstack1lll111l11l_opy_ = bstack111l1l_opy_ (u"ࠢࡪࡵࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡫ࡹࡧࠨᕔ")
    bstack11llll1l1ll_opy_ = bstack111l1l_opy_ (u"ࠣࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᕕ")
    bstack11llll1l111_opy_ = bstack111l1l_opy_ (u"ࠤࡨࡲࡩ࡫ࡤࡠࡣࡷࠦᕖ")
    bstack1llll11llll_opy_ = bstack111l1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠦᕗ")
    bstack1llll1llll1_opy_ = bstack111l1l_opy_ (u"ࠦࡳ࡫ࡷࡴࡧࡶࡷ࡮ࡵ࡮ࠣᕘ")
    bstack11llll1l1l1_opy_ = bstack111l1l_opy_ (u"ࠧ࡭ࡥࡵࠤᕙ")
    bstack1l11l11llll_opy_ = bstack111l1l_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᕚ")
    bstack1l1ll1l1lll_opy_ = bstack111l1l_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࠥᕛ")
    bstack1l1ll1ll1l1_opy_ = bstack111l1l_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࡥࡸࡿ࡮ࡤࠤᕜ")
    bstack11llll11lll_opy_ = bstack111l1l_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᕝ")
    bstack1l111111ll1_opy_: Dict[str, List[Callable]] = dict()
    bstack1llll11ll1l_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll11lll1_opy_: Any
    bstack1l1lll11111_opy_: Dict
    def __init__(
        self,
        bstack1llll11ll1l_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1llll11lll1_opy_: Dict[str, Any],
        methods=[bstack111l1l_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧᕞ"), bstack111l1l_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࠦᕟ"), bstack111l1l_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࠨᕠ"), bstack111l1l_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᕡ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1llll11ll1l_opy_ = bstack1llll11ll1l_opy_
        self.platform_index = platform_index
        self.bstack1l1lll111l1_opy_(methods)
        self.bstack1llll11lll1_opy_ = bstack1llll11lll1_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll111l1l1_opy_.get_data(bstack1lllll11111_opy_.bstack1lll1l11l1l_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll111l1l1_opy_.get_data(bstack1lllll11111_opy_.bstack1lll1l11lll_opy_, target, strict)
    @staticmethod
    def bstack11llll11l11_opy_(target: object, strict=True):
        return bstack1lll111l1l1_opy_.get_data(bstack1lllll11111_opy_.bstack11llll11ll1_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll111l1l1_opy_.get_data(bstack1lllll11111_opy_.bstack1lll1l1l11l_opy_, target, strict)
    @staticmethod
    def bstack1lll11l1111_opy_(instance: bstack1lllllll1l1_opy_) -> bool:
        return bstack1lll111l1l1_opy_.get_state(instance, bstack1lllll11111_opy_.bstack1lll111l11l_opy_, False)
    @staticmethod
    def bstack1l1ll1llll1_opy_(instance: bstack1lllllll1l1_opy_, default_value=None):
        return bstack1lll111l1l1_opy_.get_state(instance, bstack1lllll11111_opy_.bstack1lll1l11lll_opy_, default_value)
    @staticmethod
    def bstack1l1ll1l11ll_opy_(instance: bstack1lllllll1l1_opy_, default_value=None):
        return bstack1lll111l1l1_opy_.get_state(instance, bstack1lllll11111_opy_.bstack1lll1l1l11l_opy_, default_value)
    @staticmethod
    def bstack1ll1lll1lll_opy_(hub_url: str, bstack11llll11l1l_opy_=bstack111l1l_opy_ (u"ࠢ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠦᕢ")):
        try:
            bstack11llll1l11l_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll1l11l_opy_.endswith(bstack11llll11l1l_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1ll1lllll_opy_(method_name: str):
        return method_name == bstack111l1l_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᕣ")
    @staticmethod
    def bstack1llll11l1ll_opy_(method_name: str, *args):
        return (
            bstack1lllll11111_opy_.bstack1l1ll1lllll_opy_(method_name)
            and bstack1lllll11111_opy_.bstack1lllllll11l_opy_(*args) == bstack1lllll11111_opy_.bstack1llll1llll1_opy_
        )
    @staticmethod
    def bstack1l1lll11l1l_opy_(method_name: str, *args):
        if not bstack1lllll11111_opy_.bstack1l1ll1lllll_opy_(method_name):
            return False
        if not bstack1lllll11111_opy_.bstack1l1ll1l1lll_opy_ in bstack1lllll11111_opy_.bstack1lllllll11l_opy_(*args):
            return False
        bstack1l1lll1111l_opy_ = bstack1lllll11111_opy_.bstack1l1ll1ll111_opy_(*args)
        return bstack1l1lll1111l_opy_ and bstack111l1l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᕤ") in bstack1l1lll1111l_opy_ and bstack111l1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕥ") in bstack1l1lll1111l_opy_[bstack111l1l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᕦ")]
    @staticmethod
    def bstack1l1lll11l11_opy_(method_name: str, *args):
        if not bstack1lllll11111_opy_.bstack1l1ll1lllll_opy_(method_name):
            return False
        if not bstack1lllll11111_opy_.bstack1l1ll1l1lll_opy_ in bstack1lllll11111_opy_.bstack1lllllll11l_opy_(*args):
            return False
        bstack1l1lll1111l_opy_ = bstack1lllll11111_opy_.bstack1l1ll1ll111_opy_(*args)
        return (
            bstack1l1lll1111l_opy_
            and bstack111l1l_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᕧ") in bstack1l1lll1111l_opy_
            and bstack111l1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡧࡷ࡯ࡰࡵࠤᕨ") in bstack1l1lll1111l_opy_[bstack111l1l_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᕩ")]
        )
    @staticmethod
    def bstack1lllllll11l_opy_(*args):
        return str(bstack1lllll11111_opy_.bstack1l1ll1ll11l_opy_(*args)).lower()
    @staticmethod
    def bstack1l1ll1ll11l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1ll1ll111_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack1lll11llll_opy_(driver):
        command_executor = getattr(driver, bstack111l1l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕪ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack111l1l_opy_ (u"ࠤࡢࡹࡷࡲࠢᕫ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack111l1l_opy_ (u"ࠥࡣࡨࡲࡩࡦࡰࡷࡣࡨࡵ࡮ࡧ࡫ࡪࠦᕬ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack111l1l_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡣࡸ࡫ࡲࡷࡧࡵࡣࡦࡪࡤࡳࠤᕭ"), None)
        return hub_url
    def bstack1llll11l111_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack111l1l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᕮ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack111l1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕯ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack111l1l_opy_ (u"ࠢࡠࡷࡵࡰࠧᕰ")):
                setattr(command_executor, bstack111l1l_opy_ (u"ࠣࡡࡸࡶࡱࠨᕱ"), hub_url)
                result = True
        if result:
            self.bstack1llll11ll1l_opy_ = hub_url
            bstack1lllll11111_opy_.bstack1llll1l111l_opy_(instance, bstack1lllll11111_opy_.bstack1lll1l11lll_opy_, hub_url)
            bstack1lllll11111_opy_.bstack1llll1l111l_opy_(
                instance, bstack1lllll11111_opy_.bstack1lll111l11l_opy_, bstack1lllll11111_opy_.bstack1ll1lll1lll_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1lll1l11l_opy_(bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_]):
        return bstack111l1l_opy_ (u"ࠤ࠽ࠦᕲ").join((bstack1llll1lll1l_opy_(bstack1llll1l11l1_opy_[0]).name, bstack1lllll1l1ll_opy_(bstack1llll1l11l1_opy_[1]).name))
    @staticmethod
    def bstack1lllllll111_opy_(bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_], callback: Callable):
        bstack1l1lll1l111_opy_ = bstack1lllll11111_opy_.bstack1l1lll1l11l_opy_(bstack1llll1l11l1_opy_)
        if not bstack1l1lll1l111_opy_ in bstack1lllll11111_opy_.bstack1l111111ll1_opy_:
            bstack1lllll11111_opy_.bstack1l111111ll1_opy_[bstack1l1lll1l111_opy_] = []
        bstack1lllll11111_opy_.bstack1l111111ll1_opy_[bstack1l1lll1l111_opy_].append(callback)
    def bstack1l1ll1l11l1_opy_(self, instance: bstack1lllllll1l1_opy_, method_name: str, bstack1l1lll11lll_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack111l1l_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࠥᕳ")):
            return
        cmd = args[0] if method_name == bstack111l1l_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᕴ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll111ll_opy_ = bstack111l1l_opy_ (u"ࠧࡀࠢᕵ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠢᕶ") + bstack11llll111ll_opy_, bstack1l1lll11lll_opy_)
    def bstack1l1ll1l1ll1_opy_(
        self,
        target: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll111ll_opy_, bstack1l1lll11ll1_opy_ = bstack1llll1l11l1_opy_
        bstack1l1lll1l111_opy_ = bstack1lllll11111_opy_.bstack1l1lll1l11l_opy_(bstack1llll1l11l1_opy_)
        self.logger.debug(bstack111l1l_opy_ (u"ࠢࡰࡰࡢ࡬ࡴࡵ࡫࠻ࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᕷ") + str(kwargs) + bstack111l1l_opy_ (u"ࠣࠤᕸ"))
        if bstack1l1lll111ll_opy_ == bstack1llll1lll1l_opy_.QUIT:
            if bstack1l1lll11ll1_opy_ == bstack1lllll1l1ll_opy_.PRE:
                bstack1ll11l11lll_opy_ = bstack1llllll11ll_opy_.bstack1ll11lllll1_opy_(EVENTS.bstack1lll1lll1l_opy_.value)
                bstack1lll111l1l1_opy_.bstack1llll1l111l_opy_(instance, EVENTS.bstack1lll1lll1l_opy_.value, bstack1ll11l11lll_opy_)
                self.logger.debug(bstack111l1l_opy_ (u"ࠤ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࢁࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠦࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠨᕹ").format(instance, method_name, bstack1l1lll111ll_opy_, bstack1l1lll11ll1_opy_))
        if bstack1l1lll111ll_opy_ == bstack1llll1lll1l_opy_.bstack1llllllllll_opy_:
            if bstack1l1lll11ll1_opy_ == bstack1lllll1l1ll_opy_.POST and not bstack1lllll11111_opy_.bstack1lll1l11l1l_opy_ in instance.data:
                session_id = getattr(target, bstack111l1l_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᕺ"), None)
                if session_id:
                    instance.data[bstack1lllll11111_opy_.bstack1lll1l11l1l_opy_] = session_id
        elif (
            bstack1l1lll111ll_opy_ == bstack1llll1lll1l_opy_.bstack1llllll1lll_opy_
            and bstack1lllll11111_opy_.bstack1lllllll11l_opy_(*args) == bstack1lllll11111_opy_.bstack1llll1llll1_opy_
        ):
            if bstack1l1lll11ll1_opy_ == bstack1lllll1l1ll_opy_.PRE:
                hub_url = bstack1lllll11111_opy_.bstack1lll11llll_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lllll11111_opy_.bstack1lll1l11lll_opy_: hub_url,
                            bstack1lllll11111_opy_.bstack1lll111l11l_opy_: bstack1lllll11111_opy_.bstack1ll1lll1lll_opy_(hub_url),
                            bstack1lllll11111_opy_.bstack1llll11llll_opy_: int(
                                os.environ.get(bstack111l1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᕻ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1lll1111l_opy_ = bstack1lllll11111_opy_.bstack1l1ll1ll111_opy_(*args)
                bstack11llll11l11_opy_ = bstack1l1lll1111l_opy_.get(bstack111l1l_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᕼ"), None) if bstack1l1lll1111l_opy_ else None
                if isinstance(bstack11llll11l11_opy_, dict):
                    instance.data[bstack1lllll11111_opy_.bstack11llll11ll1_opy_] = copy.deepcopy(bstack11llll11l11_opy_)
                    instance.data[bstack1lllll11111_opy_.bstack1lll1l1l11l_opy_] = bstack11llll11l11_opy_
            elif bstack1l1lll11ll1_opy_ == bstack1lllll1l1ll_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack111l1l_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧᕽ"), dict()).get(bstack111l1l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡊࡦࠥᕾ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lllll11111_opy_.bstack1lll1l11l1l_opy_: framework_session_id,
                                bstack1lllll11111_opy_.bstack11llll1l1ll_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1lll111ll_opy_ == bstack1llll1lll1l_opy_.bstack1llllll1lll_opy_
            and bstack1lllll11111_opy_.bstack1lllllll11l_opy_(*args) == bstack1lllll11111_opy_.bstack11llll11lll_opy_
            and bstack1l1lll11ll1_opy_ == bstack1lllll1l1ll_opy_.POST
        ):
            instance.data[bstack1lllll11111_opy_.bstack11llll1l111_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1lll1l111_opy_ in bstack1lllll11111_opy_.bstack1l111111ll1_opy_:
            bstack1l1ll1l1l11_opy_ = None
            for callback in bstack1lllll11111_opy_.bstack1l111111ll1_opy_[bstack1l1lll1l111_opy_]:
                try:
                    bstack1l1ll1lll1l_opy_ = callback(self, target, exec, bstack1llll1l11l1_opy_, result, *args, **kwargs)
                    if bstack1l1ll1l1l11_opy_ == None:
                        bstack1l1ll1l1l11_opy_ = bstack1l1ll1lll1l_opy_
                except Exception as e:
                    self.logger.error(bstack111l1l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࠨᕿ") + str(e) + bstack111l1l_opy_ (u"ࠤࠥᖀ"))
                    traceback.print_exc()
            if bstack1l1lll111ll_opy_ == bstack1llll1lll1l_opy_.QUIT:
                if bstack1l1lll11ll1_opy_ == bstack1lllll1l1ll_opy_.POST:
                    bstack1ll11l11lll_opy_ = bstack1lll111l1l1_opy_.get_state(instance, EVENTS.bstack1lll1lll1l_opy_.value)
                    if bstack1ll11l11lll_opy_!=None:
                        bstack1llllll11ll_opy_.end(EVENTS.bstack1lll1lll1l_opy_.value, bstack1ll11l11lll_opy_+bstack111l1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᖁ"), bstack1ll11l11lll_opy_+bstack111l1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᖂ"), True, None)
            if bstack1l1lll11ll1_opy_ == bstack1lllll1l1ll_opy_.PRE and callable(bstack1l1ll1l1l11_opy_):
                return bstack1l1ll1l1l11_opy_
            elif bstack1l1lll11ll1_opy_ == bstack1lllll1l1ll_opy_.POST and bstack1l1ll1l1l11_opy_:
                return bstack1l1ll1l1l11_opy_
    def bstack1l1ll1l1l1l_opy_(
        self, method_name, previous_state: bstack1llll1lll1l_opy_, *args, **kwargs
    ) -> bstack1llll1lll1l_opy_:
        if method_name == bstack111l1l_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢᖃ") or method_name == bstack111l1l_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᖄ"):
            return bstack1llll1lll1l_opy_.bstack1llllllllll_opy_
        if method_name == bstack111l1l_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᖅ"):
            return bstack1llll1lll1l_opy_.QUIT
        if method_name == bstack111l1l_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᖆ"):
            if previous_state != bstack1llll1lll1l_opy_.NONE:
                command_name = bstack1lllll11111_opy_.bstack1lllllll11l_opy_(*args)
                if command_name == bstack1lllll11111_opy_.bstack1llll1llll1_opy_:
                    return bstack1llll1lll1l_opy_.bstack1llllllllll_opy_
            return bstack1llll1lll1l_opy_.bstack1llllll1lll_opy_
        return bstack1llll1lll1l_opy_.NONE