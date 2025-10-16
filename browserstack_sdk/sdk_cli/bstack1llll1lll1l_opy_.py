# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1lll11ll1l1_opy_,
    bstack111111lll1_opy_,
    bstack1lllllll1ll_opy_,
    bstack111111111l_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack11l111l1l_opy_ import bstack1llll1lllll_opy_
from bstack_utils.constants import EVENTS
class bstack1lllll11ll1_opy_(bstack1lll11ll1l1_opy_):
    bstack1l1llll11ll_opy_ = bstack1ll11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨᔰ")
    NAME = bstack1ll11_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᔱ")
    bstack1lll1l1l1ll_opy_ = bstack1ll11_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭ࠤᔲ")
    bstack1lll1ll1l11_opy_ = bstack1ll11_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᔳ")
    bstack11lllll1l1l_opy_ = bstack1ll11_opy_ (u"ࠥ࡭ࡳࡶࡵࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᔴ")
    bstack1lll1l1lll1_opy_ = bstack1ll11_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᔵ")
    bstack1lll11l1lll_opy_ = bstack1ll11_opy_ (u"ࠧ࡯ࡳࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡩࡷࡥࠦᔶ")
    bstack11llllll111_opy_ = bstack1ll11_opy_ (u"ࠨࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᔷ")
    bstack11lllll11ll_opy_ = bstack1ll11_opy_ (u"ࠢࡦࡰࡧࡩࡩࡥࡡࡵࠤᔸ")
    bstack1lllll111ll_opy_ = bstack1ll11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࠤᔹ")
    bstack1llllll1ll1_opy_ = bstack1ll11_opy_ (u"ࠤࡱࡩࡼࡹࡥࡴࡵ࡬ࡳࡳࠨᔺ")
    bstack11lllll1lll_opy_ = bstack1ll11_opy_ (u"ࠥ࡫ࡪࡺࠢᔻ")
    bstack1l11l11l1ll_opy_ = bstack1ll11_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᔼ")
    bstack1l1lll11lll_opy_ = bstack1ll11_opy_ (u"ࠧࡽ࠳ࡤࡧࡻࡩࡨࡻࡴࡦࡵࡦࡶ࡮ࡶࡴࠣᔽ")
    bstack1l1ll1lllll_opy_ = bstack1ll11_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࡣࡶࡽࡳࡩࠢᔾ")
    bstack11lllll1ll1_opy_ = bstack1ll11_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᔿ")
    bstack1l1111l11l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1llll1ll111_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1111111l11_opy_: Any
    bstack1l1lll1ll1l_opy_: Dict
    def __init__(
        self,
        bstack1llll1ll111_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1111111l11_opy_: Dict[str, Any],
        methods=[bstack1ll11_opy_ (u"ࠣࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠥᕀ"), bstack1ll11_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᕁ"), bstack1ll11_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦᕂ"), bstack1ll11_opy_ (u"ࠦࡶࡻࡩࡵࠤᕃ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1llll1ll111_opy_ = bstack1llll1ll111_opy_
        self.platform_index = platform_index
        self.bstack1l1lll1l1l1_opy_(methods)
        self.bstack1111111l11_opy_ = bstack1111111l11_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll11ll1l1_opy_.get_data(bstack1lllll11ll1_opy_.bstack1lll1ll1l11_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll11ll1l1_opy_.get_data(bstack1lllll11ll1_opy_.bstack1lll1l1l1ll_opy_, target, strict)
    @staticmethod
    def bstack11lllll111l_opy_(target: object, strict=True):
        return bstack1lll11ll1l1_opy_.get_data(bstack1lllll11ll1_opy_.bstack11lllll1l1l_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll11ll1l1_opy_.get_data(bstack1lllll11ll1_opy_.bstack1lll1l1lll1_opy_, target, strict)
    @staticmethod
    def bstack1lll11l111l_opy_(instance: bstack111111lll1_opy_) -> bool:
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1lllll11ll1_opy_.bstack1lll11l1lll_opy_, False)
    @staticmethod
    def bstack1l1lll1111l_opy_(instance: bstack111111lll1_opy_, default_value=None):
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1lllll11ll1_opy_.bstack1lll1l1l1ll_opy_, default_value)
    @staticmethod
    def bstack1l1lll111l1_opy_(instance: bstack111111lll1_opy_, default_value=None):
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1lllll11ll1_opy_.bstack1lll1l1lll1_opy_, default_value)
    @staticmethod
    def bstack1lll1111l1l_opy_(hub_url: str, bstack11lllll1111_opy_=bstack1ll11_opy_ (u"ࠧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠤᕄ")):
        try:
            bstack11lllll11l1_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11lllll11l1_opy_.endswith(bstack11lllll1111_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll1lll1_opy_(method_name: str):
        return method_name == bstack1ll11_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢᕅ")
    @staticmethod
    def bstack1lllll111l1_opy_(method_name: str, *args):
        return (
            bstack1lllll11ll1_opy_.bstack1l1lll1lll1_opy_(method_name)
            and bstack1lllll11ll1_opy_.bstack1lllll1ll11_opy_(*args) == bstack1lllll11ll1_opy_.bstack1llllll1ll1_opy_
        )
    @staticmethod
    def bstack1l1lll111ll_opy_(method_name: str, *args):
        if not bstack1lllll11ll1_opy_.bstack1l1lll1lll1_opy_(method_name):
            return False
        if not bstack1lllll11ll1_opy_.bstack1l1lll11lll_opy_ in bstack1lllll11ll1_opy_.bstack1lllll1ll11_opy_(*args):
            return False
        bstack1l1llll1111_opy_ = bstack1lllll11ll1_opy_.bstack1l1lll11111_opy_(*args)
        return bstack1l1llll1111_opy_ and bstack1ll11_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᕆ") in bstack1l1llll1111_opy_ and bstack1ll11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕇ") in bstack1l1llll1111_opy_[bstack1ll11_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᕈ")]
    @staticmethod
    def bstack1l1lll11l11_opy_(method_name: str, *args):
        if not bstack1lllll11ll1_opy_.bstack1l1lll1lll1_opy_(method_name):
            return False
        if not bstack1lllll11ll1_opy_.bstack1l1lll11lll_opy_ in bstack1lllll11ll1_opy_.bstack1lllll1ll11_opy_(*args):
            return False
        bstack1l1llll1111_opy_ = bstack1lllll11ll1_opy_.bstack1l1lll11111_opy_(*args)
        return (
            bstack1l1llll1111_opy_
            and bstack1ll11_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᕉ") in bstack1l1llll1111_opy_
            and bstack1ll11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡥࡵ࡭ࡵࡺࠢᕊ") in bstack1l1llll1111_opy_[bstack1ll11_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᕋ")]
        )
    @staticmethod
    def bstack1lllll1ll11_opy_(*args):
        return str(bstack1lllll11ll1_opy_.bstack1l1lll11ll1_opy_(*args)).lower()
    @staticmethod
    def bstack1l1lll11ll1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll11111_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack1ll1ll111l_opy_(driver):
        command_executor = getattr(driver, bstack1ll11_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕌ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1ll11_opy_ (u"ࠢࡠࡷࡵࡰࠧᕍ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1ll11_opy_ (u"ࠣࡡࡦࡰ࡮࡫࡮ࡵࡡࡦࡳࡳ࡬ࡩࡨࠤᕎ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1ll11_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦࡡࡶࡩࡷࡼࡥࡳࡡࡤࡨࡩࡸࠢᕏ"), None)
        return hub_url
    def bstack111111l1l1_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1ll11_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨᕐ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1ll11_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᕑ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1ll11_opy_ (u"ࠧࡥࡵࡳ࡮ࠥᕒ")):
                setattr(command_executor, bstack1ll11_opy_ (u"ࠨ࡟ࡶࡴ࡯ࠦᕓ"), hub_url)
                result = True
        if result:
            self.bstack1llll1ll111_opy_ = hub_url
            bstack1lllll11ll1_opy_.bstack1llll1ll1ll_opy_(instance, bstack1lllll11ll1_opy_.bstack1lll1l1l1ll_opy_, hub_url)
            bstack1lllll11ll1_opy_.bstack1llll1ll1ll_opy_(
                instance, bstack1lllll11ll1_opy_.bstack1lll11l1lll_opy_, bstack1lllll11ll1_opy_.bstack1lll1111l1l_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1lll1ll11_opy_(bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_]):
        return bstack1ll11_opy_ (u"ࠢ࠻ࠤᕔ").join((bstack1lllllll1ll_opy_(bstack1llll1l1ll1_opy_[0]).name, bstack111111111l_opy_(bstack1llll1l1ll1_opy_[1]).name))
    @staticmethod
    def bstack11111111l1_opy_(bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_], callback: Callable):
        bstack1l1lll1l111_opy_ = bstack1lllll11ll1_opy_.bstack1l1lll1ll11_opy_(bstack1llll1l1ll1_opy_)
        if not bstack1l1lll1l111_opy_ in bstack1lllll11ll1_opy_.bstack1l1111l11l1_opy_:
            bstack1lllll11ll1_opy_.bstack1l1111l11l1_opy_[bstack1l1lll1l111_opy_] = []
        bstack1lllll11ll1_opy_.bstack1l1111l11l1_opy_[bstack1l1lll1l111_opy_].append(callback)
    def bstack1l1lll1l11l_opy_(self, instance: bstack111111lll1_opy_, method_name: str, bstack1l1llll1ll1_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1ll11_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣᕕ")):
            return
        cmd = args[0] if method_name == bstack1ll11_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࠥᕖ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11lllll1l11_opy_ = bstack1ll11_opy_ (u"ࠥ࠾ࠧᕗ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠧᕘ") + bstack11lllll1l11_opy_, bstack1l1llll1ll1_opy_)
    def bstack1l1llll11l1_opy_(
        self,
        target: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1llll111l_opy_, bstack1l1llll1l1l_opy_ = bstack1llll1l1ll1_opy_
        bstack1l1lll1l111_opy_ = bstack1lllll11ll1_opy_.bstack1l1lll1ll11_opy_(bstack1llll1l1ll1_opy_)
        self.logger.debug(bstack1ll11_opy_ (u"ࠧࡵ࡮ࡠࡪࡲࡳࡰࡀࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᕙ") + str(kwargs) + bstack1ll11_opy_ (u"ࠨࠢᕚ"))
        if bstack1l1llll111l_opy_ == bstack1lllllll1ll_opy_.QUIT:
            if bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.PRE:
                bstack1ll1l1ll1l1_opy_ = bstack1llll1lllll_opy_.bstack1ll111lll1l_opy_(EVENTS.bstack11l1lll1ll_opy_.value)
                bstack1lll11ll1l1_opy_.bstack1llll1ll1ll_opy_(instance, EVENTS.bstack11l1lll1ll_opy_.value, bstack1ll1l1ll1l1_opy_)
                self.logger.debug(bstack1ll11_opy_ (u"ࠢࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾࢁࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࡿࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠤ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠦᕛ").format(instance, method_name, bstack1l1llll111l_opy_, bstack1l1llll1l1l_opy_))
        if bstack1l1llll111l_opy_ == bstack1lllllll1ll_opy_.bstack1lllllll1l1_opy_:
            if bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.POST and not bstack1lllll11ll1_opy_.bstack1lll1ll1l11_opy_ in instance.data:
                session_id = getattr(target, bstack1ll11_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧᕜ"), None)
                if session_id:
                    instance.data[bstack1lllll11ll1_opy_.bstack1lll1ll1l11_opy_] = session_id
        elif (
            bstack1l1llll111l_opy_ == bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_
            and bstack1lllll11ll1_opy_.bstack1lllll1ll11_opy_(*args) == bstack1lllll11ll1_opy_.bstack1llllll1ll1_opy_
        ):
            if bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.PRE:
                hub_url = bstack1lllll11ll1_opy_.bstack1ll1ll111l_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lllll11ll1_opy_.bstack1lll1l1l1ll_opy_: hub_url,
                            bstack1lllll11ll1_opy_.bstack1lll11l1lll_opy_: bstack1lllll11ll1_opy_.bstack1lll1111l1l_opy_(hub_url),
                            bstack1lllll11ll1_opy_.bstack1lllll111ll_opy_: int(
                                os.environ.get(bstack1ll11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤᕝ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1llll1111_opy_ = bstack1lllll11ll1_opy_.bstack1l1lll11111_opy_(*args)
                bstack11lllll111l_opy_ = bstack1l1llll1111_opy_.get(bstack1ll11_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᕞ"), None) if bstack1l1llll1111_opy_ else None
                if isinstance(bstack11lllll111l_opy_, dict):
                    instance.data[bstack1lllll11ll1_opy_.bstack11lllll1l1l_opy_] = copy.deepcopy(bstack11lllll111l_opy_)
                    instance.data[bstack1lllll11ll1_opy_.bstack1lll1l1lll1_opy_] = bstack11lllll111l_opy_
            elif bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1ll11_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥᕟ"), dict()).get(bstack1ll11_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡏࡤࠣᕠ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lllll11ll1_opy_.bstack1lll1ll1l11_opy_: framework_session_id,
                                bstack1lllll11ll1_opy_.bstack11llllll111_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1llll111l_opy_ == bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_
            and bstack1lllll11ll1_opy_.bstack1lllll1ll11_opy_(*args) == bstack1lllll11ll1_opy_.bstack11lllll1ll1_opy_
            and bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.POST
        ):
            instance.data[bstack1lllll11ll1_opy_.bstack11lllll11ll_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1lll1l111_opy_ in bstack1lllll11ll1_opy_.bstack1l1111l11l1_opy_:
            bstack1l1llll1l11_opy_ = None
            for callback in bstack1lllll11ll1_opy_.bstack1l1111l11l1_opy_[bstack1l1lll1l111_opy_]:
                try:
                    bstack1l1lll1l1ll_opy_ = callback(self, target, exec, bstack1llll1l1ll1_opy_, result, *args, **kwargs)
                    if bstack1l1llll1l11_opy_ == None:
                        bstack1l1llll1l11_opy_ = bstack1l1lll1l1ll_opy_
                except Exception as e:
                    self.logger.error(bstack1ll11_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࠦᕡ") + str(e) + bstack1ll11_opy_ (u"ࠢࠣᕢ"))
                    traceback.print_exc()
            if bstack1l1llll111l_opy_ == bstack1lllllll1ll_opy_.QUIT:
                if bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.POST:
                    bstack1ll1l1ll1l1_opy_ = bstack1lll11ll1l1_opy_.get_state(instance, EVENTS.bstack11l1lll1ll_opy_.value)
                    if bstack1ll1l1ll1l1_opy_!=None:
                        bstack1llll1lllll_opy_.end(EVENTS.bstack11l1lll1ll_opy_.value, bstack1ll1l1ll1l1_opy_+bstack1ll11_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᕣ"), bstack1ll1l1ll1l1_opy_+bstack1ll11_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᕤ"), True, None)
            if bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.PRE and callable(bstack1l1llll1l11_opy_):
                return bstack1l1llll1l11_opy_
            elif bstack1l1llll1l1l_opy_ == bstack111111111l_opy_.POST and bstack1l1llll1l11_opy_:
                return bstack1l1llll1l11_opy_
    def bstack1l1lll1llll_opy_(
        self, method_name, previous_state: bstack1lllllll1ll_opy_, *args, **kwargs
    ) -> bstack1lllllll1ll_opy_:
        if method_name == bstack1ll11_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧᕥ") or method_name == bstack1ll11_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࠦᕦ"):
            return bstack1lllllll1ll_opy_.bstack1lllllll1l1_opy_
        if method_name == bstack1ll11_opy_ (u"ࠧࡷࡵࡪࡶࠥᕧ"):
            return bstack1lllllll1ll_opy_.QUIT
        if method_name == bstack1ll11_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢᕨ"):
            if previous_state != bstack1lllllll1ll_opy_.NONE:
                command_name = bstack1lllll11ll1_opy_.bstack1lllll1ll11_opy_(*args)
                if command_name == bstack1lllll11ll1_opy_.bstack1llllll1ll1_opy_:
                    return bstack1lllllll1ll_opy_.bstack1lllllll1l1_opy_
            return bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_
        return bstack1lllllll1ll_opy_.NONE