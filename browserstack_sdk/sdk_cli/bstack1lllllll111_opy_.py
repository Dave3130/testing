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
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import (
    bstack1lll11l1111_opy_,
    bstack1llllllll1l_opy_,
    bstack1lllll11l1l_opy_,
    bstack1111111lll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack111l11llll_opy_ import bstack1llll1l1l11_opy_
from bstack_utils.constants import EVENTS
class bstack1lllll11l11_opy_(bstack1lll11l1111_opy_):
    bstack1l1lll1ll1l_opy_ = bstack1ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣᔫ")
    NAME = bstack1ll1l_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᔬ")
    bstack1llll11l11l_opy_ = bstack1ll1l_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࠦᔭ")
    bstack1lll1l1llll_opy_ = bstack1ll1l_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᔮ")
    bstack11lllll11ll_opy_ = bstack1ll1l_opy_ (u"ࠧ࡯࡮ࡱࡷࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᔯ")
    bstack1lll1l1111l_opy_ = bstack1ll1l_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᔰ")
    bstack1lll11ll1l1_opy_ = bstack1ll1l_opy_ (u"ࠢࡪࡵࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡫ࡹࡧࠨᔱ")
    bstack11llll1lll1_opy_ = bstack1ll1l_opy_ (u"ࠣࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᔲ")
    bstack11lllll1111_opy_ = bstack1ll1l_opy_ (u"ࠤࡨࡲࡩ࡫ࡤࡠࡣࡷࠦᔳ")
    bstack1lllllllll1_opy_ = bstack1ll1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠦᔴ")
    bstack1llllll1l1l_opy_ = bstack1ll1l_opy_ (u"ࠦࡳ࡫ࡷࡴࡧࡶࡷ࡮ࡵ࡮ࠣᔵ")
    bstack11lllll1ll1_opy_ = bstack1ll1l_opy_ (u"ࠧ࡭ࡥࡵࠤᔶ")
    bstack1l11ll11ll1_opy_ = bstack1ll1l_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᔷ")
    bstack1l1lll111l1_opy_ = bstack1ll1l_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࠥᔸ")
    bstack1l1llll1l11_opy_ = bstack1ll1l_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࡥࡸࡿ࡮ࡤࠤᔹ")
    bstack11lllll11l1_opy_ = bstack1ll1l_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᔺ")
    bstack1l1111l1l1l_opy_: Dict[str, List[Callable]] = dict()
    bstack1lllllll1l1_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1l11ll_opy_: Any
    bstack1l1lll11l1l_opy_: Dict
    def __init__(
        self,
        bstack1lllllll1l1_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1llll1l11ll_opy_: Dict[str, Any],
        methods=[bstack1ll1l_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧᔻ"), bstack1ll1l_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࠦᔼ"), bstack1ll1l_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࠨᔽ"), bstack1ll1l_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᔾ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1lllllll1l1_opy_ = bstack1lllllll1l1_opy_
        self.platform_index = platform_index
        self.bstack1l1lll111ll_opy_(methods)
        self.bstack1llll1l11ll_opy_ = bstack1llll1l11ll_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll11l1111_opy_.get_data(bstack1lllll11l11_opy_.bstack1lll1l1llll_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll11l1111_opy_.get_data(bstack1lllll11l11_opy_.bstack1llll11l11l_opy_, target, strict)
    @staticmethod
    def bstack11lllll1l1l_opy_(target: object, strict=True):
        return bstack1lll11l1111_opy_.get_data(bstack1lllll11l11_opy_.bstack11lllll11ll_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll11l1111_opy_.get_data(bstack1lllll11l11_opy_.bstack1lll1l1111l_opy_, target, strict)
    @staticmethod
    def bstack1lll111ll1l_opy_(instance: bstack1llllllll1l_opy_) -> bool:
        return bstack1lll11l1111_opy_.get_state(instance, bstack1lllll11l11_opy_.bstack1lll11ll1l1_opy_, False)
    @staticmethod
    def bstack1l1lll11111_opy_(instance: bstack1llllllll1l_opy_, default_value=None):
        return bstack1lll11l1111_opy_.get_state(instance, bstack1lllll11l11_opy_.bstack1llll11l11l_opy_, default_value)
    @staticmethod
    def bstack1l1lll1lll1_opy_(instance: bstack1llllllll1l_opy_, default_value=None):
        return bstack1lll11l1111_opy_.get_state(instance, bstack1lllll11l11_opy_.bstack1lll1l1111l_opy_, default_value)
    @staticmethod
    def bstack1lll1111l11_opy_(hub_url: str, bstack11lllll1l11_opy_=bstack1ll1l_opy_ (u"ࠢ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠦᔿ")):
        try:
            bstack11lllll111l_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11lllll111l_opy_.endswith(bstack11lllll1l11_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll1l1ll_opy_(method_name: str):
        return method_name == bstack1ll1l_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᕀ")
    @staticmethod
    def bstack1lllll1111l_opy_(method_name: str, *args):
        return (
            bstack1lllll11l11_opy_.bstack1l1lll1l1ll_opy_(method_name)
            and bstack1lllll11l11_opy_.bstack1111111l1l_opy_(*args) == bstack1lllll11l11_opy_.bstack1llllll1l1l_opy_
        )
    @staticmethod
    def bstack1l1lll1l111_opy_(method_name: str, *args):
        if not bstack1lllll11l11_opy_.bstack1l1lll1l1ll_opy_(method_name):
            return False
        if not bstack1lllll11l11_opy_.bstack1l1lll111l1_opy_ in bstack1lllll11l11_opy_.bstack1111111l1l_opy_(*args):
            return False
        bstack1l1llll1111_opy_ = bstack1lllll11l11_opy_.bstack1l1llll111l_opy_(*args)
        return bstack1l1llll1111_opy_ and bstack1ll1l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᕁ") in bstack1l1llll1111_opy_ and bstack1ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕂ") in bstack1l1llll1111_opy_[bstack1ll1l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᕃ")]
    @staticmethod
    def bstack1l1lll1l1l1_opy_(method_name: str, *args):
        if not bstack1lllll11l11_opy_.bstack1l1lll1l1ll_opy_(method_name):
            return False
        if not bstack1lllll11l11_opy_.bstack1l1lll111l1_opy_ in bstack1lllll11l11_opy_.bstack1111111l1l_opy_(*args):
            return False
        bstack1l1llll1111_opy_ = bstack1lllll11l11_opy_.bstack1l1llll111l_opy_(*args)
        return (
            bstack1l1llll1111_opy_
            and bstack1ll1l_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᕄ") in bstack1l1llll1111_opy_
            and bstack1ll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡧࡷ࡯ࡰࡵࠤᕅ") in bstack1l1llll1111_opy_[bstack1ll1l_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᕆ")]
        )
    @staticmethod
    def bstack1111111l1l_opy_(*args):
        return str(bstack1lllll11l11_opy_.bstack1l1lll1l11l_opy_(*args)).lower()
    @staticmethod
    def bstack1l1lll1l11l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1llll111l_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack1l1l1llll_opy_(driver):
        command_executor = getattr(driver, bstack1ll1l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕇ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1ll1l_opy_ (u"ࠤࡢࡹࡷࡲࠢᕈ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1ll1l_opy_ (u"ࠥࡣࡨࡲࡩࡦࡰࡷࡣࡨࡵ࡮ࡧ࡫ࡪࠦᕉ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1ll1l_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡣࡸ࡫ࡲࡷࡧࡵࡣࡦࡪࡤࡳࠤᕊ"), None)
        return hub_url
    def bstack1llllll11l1_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1ll1l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᕋ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕌ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1ll1l_opy_ (u"ࠢࡠࡷࡵࡰࠧᕍ")):
                setattr(command_executor, bstack1ll1l_opy_ (u"ࠣࡡࡸࡶࡱࠨᕎ"), hub_url)
                result = True
        if result:
            self.bstack1lllllll1l1_opy_ = hub_url
            bstack1lllll11l11_opy_.bstack1111111ll1_opy_(instance, bstack1lllll11l11_opy_.bstack1llll11l11l_opy_, hub_url)
            bstack1lllll11l11_opy_.bstack1111111ll1_opy_(
                instance, bstack1lllll11l11_opy_.bstack1lll11ll1l1_opy_, bstack1lllll11l11_opy_.bstack1lll1111l11_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1llll1l1l_opy_(bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_]):
        return bstack1ll1l_opy_ (u"ࠤ࠽ࠦᕏ").join((bstack1lllll11l1l_opy_(bstack1llllll111l_opy_[0]).name, bstack1111111lll_opy_(bstack1llllll111l_opy_[1]).name))
    @staticmethod
    def bstack1lllll1l11l_opy_(bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_], callback: Callable):
        bstack1l1ll1lllll_opy_ = bstack1lllll11l11_opy_.bstack1l1llll1l1l_opy_(bstack1llllll111l_opy_)
        if not bstack1l1ll1lllll_opy_ in bstack1lllll11l11_opy_.bstack1l1111l1l1l_opy_:
            bstack1lllll11l11_opy_.bstack1l1111l1l1l_opy_[bstack1l1ll1lllll_opy_] = []
        bstack1lllll11l11_opy_.bstack1l1111l1l1l_opy_[bstack1l1ll1lllll_opy_].append(callback)
    def bstack1l1lll1111l_opy_(self, instance: bstack1llllllll1l_opy_, method_name: str, bstack1l1lll1ll11_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1ll1l_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࠥᕐ")):
            return
        cmd = args[0] if method_name == bstack1ll1l_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᕑ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll1llll_opy_ = bstack1ll1l_opy_ (u"ࠧࡀࠢᕒ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠢᕓ") + bstack11llll1llll_opy_, bstack1l1lll1ll11_opy_)
    def bstack1l1llll11ll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll11ll1_opy_, bstack1l1lll1llll_opy_ = bstack1llllll111l_opy_
        bstack1l1ll1lllll_opy_ = bstack1lllll11l11_opy_.bstack1l1llll1l1l_opy_(bstack1llllll111l_opy_)
        self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡰࡰࡢ࡬ࡴࡵ࡫࠻ࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᕔ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠣࠤᕕ"))
        if bstack1l1lll11ll1_opy_ == bstack1lllll11l1l_opy_.QUIT:
            if bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.PRE:
                bstack1l1lllll111_opy_ = bstack1llll1l1l11_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack11llll111l_opy_.value)
                bstack1lll11l1111_opy_.bstack1111111ll1_opy_(instance, EVENTS.bstack11llll111l_opy_.value, bstack1l1lllll111_opy_)
                self.logger.debug(bstack1ll1l_opy_ (u"ࠤ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࢁࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠦࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠨᕖ").format(instance, method_name, bstack1l1lll11ll1_opy_, bstack1l1lll1llll_opy_))
        if bstack1l1lll11ll1_opy_ == bstack1lllll11l1l_opy_.bstack1llll1ll11l_opy_:
            if bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.POST and not bstack1lllll11l11_opy_.bstack1lll1l1llll_opy_ in instance.data:
                session_id = getattr(target, bstack1ll1l_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᕗ"), None)
                if session_id:
                    instance.data[bstack1lllll11l11_opy_.bstack1lll1l1llll_opy_] = session_id
        elif (
            bstack1l1lll11ll1_opy_ == bstack1lllll11l1l_opy_.bstack1111111111_opy_
            and bstack1lllll11l11_opy_.bstack1111111l1l_opy_(*args) == bstack1lllll11l11_opy_.bstack1llllll1l1l_opy_
        ):
            if bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.PRE:
                hub_url = bstack1lllll11l11_opy_.bstack1l1l1llll_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lllll11l11_opy_.bstack1llll11l11l_opy_: hub_url,
                            bstack1lllll11l11_opy_.bstack1lll11ll1l1_opy_: bstack1lllll11l11_opy_.bstack1lll1111l11_opy_(hub_url),
                            bstack1lllll11l11_opy_.bstack1lllllllll1_opy_: int(
                                os.environ.get(bstack1ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᕘ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1llll1111_opy_ = bstack1lllll11l11_opy_.bstack1l1llll111l_opy_(*args)
                bstack11lllll1l1l_opy_ = bstack1l1llll1111_opy_.get(bstack1ll1l_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᕙ"), None) if bstack1l1llll1111_opy_ else None
                if isinstance(bstack11lllll1l1l_opy_, dict):
                    instance.data[bstack1lllll11l11_opy_.bstack11lllll11ll_opy_] = copy.deepcopy(bstack11lllll1l1l_opy_)
                    instance.data[bstack1lllll11l11_opy_.bstack1lll1l1111l_opy_] = bstack11lllll1l1l_opy_
            elif bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1ll1l_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧᕚ"), dict()).get(bstack1ll1l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡊࡦࠥᕛ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lllll11l11_opy_.bstack1lll1l1llll_opy_: framework_session_id,
                                bstack1lllll11l11_opy_.bstack11llll1lll1_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1lll11ll1_opy_ == bstack1lllll11l1l_opy_.bstack1111111111_opy_
            and bstack1lllll11l11_opy_.bstack1111111l1l_opy_(*args) == bstack1lllll11l11_opy_.bstack11lllll11l1_opy_
            and bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.POST
        ):
            instance.data[bstack1lllll11l11_opy_.bstack11lllll1111_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1ll1lllll_opy_ in bstack1lllll11l11_opy_.bstack1l1111l1l1l_opy_:
            bstack1l1ll1llll1_opy_ = None
            for callback in bstack1lllll11l11_opy_.bstack1l1111l1l1l_opy_[bstack1l1ll1lllll_opy_]:
                try:
                    bstack1l1lll11l11_opy_ = callback(self, target, exec, bstack1llllll111l_opy_, result, *args, **kwargs)
                    if bstack1l1ll1llll1_opy_ == None:
                        bstack1l1ll1llll1_opy_ = bstack1l1lll11l11_opy_
                except Exception as e:
                    self.logger.error(bstack1ll1l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࠨᕜ") + str(e) + bstack1ll1l_opy_ (u"ࠤࠥᕝ"))
                    traceback.print_exc()
            if bstack1l1lll11ll1_opy_ == bstack1lllll11l1l_opy_.QUIT:
                if bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.POST:
                    bstack1l1lllll111_opy_ = bstack1lll11l1111_opy_.get_state(instance, EVENTS.bstack11llll111l_opy_.value)
                    if bstack1l1lllll111_opy_!=None:
                        bstack1llll1l1l11_opy_.end(EVENTS.bstack11llll111l_opy_.value, bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᕞ"), bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᕟ"), True, None)
            if bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.PRE and callable(bstack1l1ll1llll1_opy_):
                return bstack1l1ll1llll1_opy_
            elif bstack1l1lll1llll_opy_ == bstack1111111lll_opy_.POST and bstack1l1ll1llll1_opy_:
                return bstack1l1ll1llll1_opy_
    def bstack1l1lll11lll_opy_(
        self, method_name, previous_state: bstack1lllll11l1l_opy_, *args, **kwargs
    ) -> bstack1lllll11l1l_opy_:
        if method_name == bstack1ll1l_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢᕠ") or method_name == bstack1ll1l_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᕡ"):
            return bstack1lllll11l1l_opy_.bstack1llll1ll11l_opy_
        if method_name == bstack1ll1l_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᕢ"):
            return bstack1lllll11l1l_opy_.QUIT
        if method_name == bstack1ll1l_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᕣ"):
            if previous_state != bstack1lllll11l1l_opy_.NONE:
                command_name = bstack1lllll11l11_opy_.bstack1111111l1l_opy_(*args)
                if command_name == bstack1lllll11l11_opy_.bstack1llllll1l1l_opy_:
                    return bstack1lllll11l1l_opy_.bstack1llll1ll11l_opy_
            return bstack1lllll11l1l_opy_.bstack1111111111_opy_
        return bstack1lllll11l1l_opy_.NONE