# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import (
    bstack1lll111ll11_opy_,
    bstack1llllllll1l_opy_,
    bstack1llll1lll11_opy_,
    bstack1llll1ll111_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
from bstack_utils.constants import EVENTS
class bstack1lllll111l1_opy_(bstack1lll111ll11_opy_):
    bstack1l1lll11111_opy_ = bstack1l1lll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤᔬ")
    NAME = bstack1l1lll1_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧᔭ")
    bstack1lll1ll1ll1_opy_ = bstack1l1lll1_opy_ (u"ࠦ࡭ࡻࡢࡠࡷࡵࡰࠧᔮ")
    bstack1llll11llll_opy_ = bstack1l1lll1_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧᔯ")
    bstack11llll1ll1l_opy_ = bstack1l1lll1_opy_ (u"ࠨࡩ࡯ࡲࡸࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᔰ")
    bstack1lll1ll1111_opy_ = bstack1l1lll1_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᔱ")
    bstack1lll11ll11l_opy_ = bstack1l1lll1_opy_ (u"ࠣ࡫ࡶࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢ࡬ࡺࡨࠢᔲ")
    bstack11llll1llll_opy_ = bstack1l1lll1_opy_ (u"ࠤࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᔳ")
    bstack11lllll1111_opy_ = bstack1l1lll1_opy_ (u"ࠥࡩࡳࡪࡥࡥࡡࡤࡸࠧᔴ")
    bstack1llll1l1ll1_opy_ = bstack1l1lll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࠧᔵ")
    bstack1llll1l11ll_opy_ = bstack1l1lll1_opy_ (u"ࠧࡴࡥࡸࡵࡨࡷࡸ࡯࡯࡯ࠤᔶ")
    bstack11lllll11ll_opy_ = bstack1l1lll1_opy_ (u"ࠨࡧࡦࡶࠥᔷ")
    bstack1l11ll11lll_opy_ = bstack1l1lll1_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᔸ")
    bstack1l1ll1lllll_opy_ = bstack1l1lll1_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࠦᔹ")
    bstack1l1lll1ll1l_opy_ = bstack1l1lll1_opy_ (u"ࠤࡺ࠷ࡨ࡫ࡸࡦࡥࡸࡸࡪࡹࡣࡳ࡫ࡳࡸࡦࡹࡹ࡯ࡥࠥᔺ")
    bstack11lllll1l1l_opy_ = bstack1l1lll1_opy_ (u"ࠥࡵࡺ࡯ࡴࠣᔻ")
    bstack1l1111l11l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1111111lll_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lllllll11l_opy_: Any
    bstack1l1lll1ll11_opy_: Dict
    def __init__(
        self,
        bstack1111111lll_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1lllllll11l_opy_: Dict[str, Any],
        methods=[bstack1l1lll1_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨᔼ"), bstack1l1lll1_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᔽ"), bstack1l1lll1_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢᔾ"), bstack1l1lll1_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᔿ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1111111lll_opy_ = bstack1111111lll_opy_
        self.platform_index = platform_index
        self.bstack1l1lll11ll1_opy_(methods)
        self.bstack1lllllll11l_opy_ = bstack1lllllll11l_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll111ll11_opy_.get_data(bstack1lllll111l1_opy_.bstack1llll11llll_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll111ll11_opy_.get_data(bstack1lllll111l1_opy_.bstack1lll1ll1ll1_opy_, target, strict)
    @staticmethod
    def bstack11lllll111l_opy_(target: object, strict=True):
        return bstack1lll111ll11_opy_.get_data(bstack1lllll111l1_opy_.bstack11llll1ll1l_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll111ll11_opy_.get_data(bstack1lllll111l1_opy_.bstack1lll1ll1111_opy_, target, strict)
    @staticmethod
    def bstack1lll111llll_opy_(instance: bstack1llllllll1l_opy_) -> bool:
        return bstack1lll111ll11_opy_.get_state(instance, bstack1lllll111l1_opy_.bstack1lll11ll11l_opy_, False)
    @staticmethod
    def bstack1l1lll1l111_opy_(instance: bstack1llllllll1l_opy_, default_value=None):
        return bstack1lll111ll11_opy_.get_state(instance, bstack1lllll111l1_opy_.bstack1lll1ll1ll1_opy_, default_value)
    @staticmethod
    def bstack1l1lll1111l_opy_(instance: bstack1llllllll1l_opy_, default_value=None):
        return bstack1lll111ll11_opy_.get_state(instance, bstack1lllll111l1_opy_.bstack1lll1ll1111_opy_, default_value)
    @staticmethod
    def bstack1lll111l111_opy_(hub_url: str, bstack11lllll1l11_opy_=bstack1l1lll1_opy_ (u"ࠣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠧᕀ")):
        try:
            bstack11llll1lll1_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll1lll1_opy_.endswith(bstack11lllll1l11_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll1lll1_opy_(method_name: str):
        return method_name == bstack1l1lll1_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࠥᕁ")
    @staticmethod
    def bstack1111111l1l_opy_(method_name: str, *args):
        return (
            bstack1lllll111l1_opy_.bstack1l1lll1lll1_opy_(method_name)
            and bstack1lllll111l1_opy_.bstack1lllll11111_opy_(*args) == bstack1lllll111l1_opy_.bstack1llll1l11ll_opy_
        )
    @staticmethod
    def bstack1l1lll1l11l_opy_(method_name: str, *args):
        if not bstack1lllll111l1_opy_.bstack1l1lll1lll1_opy_(method_name):
            return False
        if not bstack1lllll111l1_opy_.bstack1l1ll1lllll_opy_ in bstack1lllll111l1_opy_.bstack1lllll11111_opy_(*args):
            return False
        bstack1l1lll11lll_opy_ = bstack1lllll111l1_opy_.bstack1l1lll1l1ll_opy_(*args)
        return bstack1l1lll11lll_opy_ and bstack1l1lll1_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᕂ") in bstack1l1lll11lll_opy_ and bstack1l1lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧᕃ") in bstack1l1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᕄ")]
    @staticmethod
    def bstack1l1lll1llll_opy_(method_name: str, *args):
        if not bstack1lllll111l1_opy_.bstack1l1lll1lll1_opy_(method_name):
            return False
        if not bstack1lllll111l1_opy_.bstack1l1ll1lllll_opy_ in bstack1lllll111l1_opy_.bstack1lllll11111_opy_(*args):
            return False
        bstack1l1lll11lll_opy_ = bstack1lllll111l1_opy_.bstack1l1lll1l1ll_opy_(*args)
        return (
            bstack1l1lll11lll_opy_
            and bstack1l1lll1_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨᕅ") in bstack1l1lll11lll_opy_
            and bstack1l1lll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡨࡸࡩࡱࡶࠥᕆ") in bstack1l1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣᕇ")]
        )
    @staticmethod
    def bstack1lllll11111_opy_(*args):
        return str(bstack1lllll111l1_opy_.bstack1l1llll11l1_opy_(*args)).lower()
    @staticmethod
    def bstack1l1llll11l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll1l1ll_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack111ll1ll1l_opy_(driver):
        command_executor = getattr(driver, bstack1l1lll1_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧᕈ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1l1lll1_opy_ (u"ࠥࡣࡺࡸ࡬ࠣᕉ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1l1lll1_opy_ (u"ࠦࡤࡩ࡬ࡪࡧࡱࡸࡤࡩ࡯࡯ࡨ࡬࡫ࠧᕊ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1l1lll1_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩࡤࡹࡥࡳࡸࡨࡶࡤࡧࡤࡥࡴࠥᕋ"), None)
        return hub_url
    def bstack111111l1ll_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1l1lll1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕌ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1l1lll1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᕍ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1l1lll1_opy_ (u"ࠣࡡࡸࡶࡱࠨᕎ")):
                setattr(command_executor, bstack1l1lll1_opy_ (u"ࠤࡢࡹࡷࡲࠢᕏ"), hub_url)
                result = True
        if result:
            self.bstack1111111lll_opy_ = hub_url
            bstack1lllll111l1_opy_.bstack1llll1lllll_opy_(instance, bstack1lllll111l1_opy_.bstack1lll1ll1ll1_opy_, hub_url)
            bstack1lllll111l1_opy_.bstack1llll1lllll_opy_(
                instance, bstack1lllll111l1_opy_.bstack1lll11ll11l_opy_, bstack1lllll111l1_opy_.bstack1lll111l111_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1lll11l1l_opy_(bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_]):
        return bstack1l1lll1_opy_ (u"ࠥ࠾ࠧᕐ").join((bstack1llll1lll11_opy_(bstack1lllll1llll_opy_[0]).name, bstack1llll1ll111_opy_(bstack1lllll1llll_opy_[1]).name))
    @staticmethod
    def bstack1llllll1111_opy_(bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_], callback: Callable):
        bstack1l1lll11l11_opy_ = bstack1lllll111l1_opy_.bstack1l1lll11l1l_opy_(bstack1lllll1llll_opy_)
        if not bstack1l1lll11l11_opy_ in bstack1lllll111l1_opy_.bstack1l1111l11l1_opy_:
            bstack1lllll111l1_opy_.bstack1l1111l11l1_opy_[bstack1l1lll11l11_opy_] = []
        bstack1lllll111l1_opy_.bstack1l1111l11l1_opy_[bstack1l1lll11l11_opy_].append(callback)
    def bstack1l1llll111l_opy_(self, instance: bstack1llllllll1l_opy_, method_name: str, bstack1l1ll1lll1l_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1l1lll1_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࠦᕑ")):
            return
        cmd = args[0] if method_name == bstack1l1lll1_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࠨᕒ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11lllll11l1_opy_ = bstack1l1lll1_opy_ (u"ࠨ࠺ࠣᕓ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠣᕔ") + bstack11lllll11l1_opy_, bstack1l1ll1lll1l_opy_)
    def bstack1l1llll11ll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1llll1111_opy_, bstack1l1ll1llll1_opy_ = bstack1lllll1llll_opy_
        bstack1l1lll11l11_opy_ = bstack1lllll111l1_opy_.bstack1l1lll11l1l_opy_(bstack1lllll1llll_opy_)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡱࡱࡣ࡭ࡵ࡯࡬࠼ࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᕕ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠤࠥᕖ"))
        if bstack1l1llll1111_opy_ == bstack1llll1lll11_opy_.QUIT:
            if bstack1l1ll1llll1_opy_ == bstack1llll1ll111_opy_.PRE:
                bstack1ll1l11l111_opy_ = bstack1llll1ll11l_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack11lll1l11l_opy_.value)
                bstack1lll111ll11_opy_.bstack1llll1lllll_opy_(instance, EVENTS.bstack11lll1l11l_opy_.value, bstack1ll1l11l111_opy_)
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠥ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࢃࠠࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࢃࠢᕗ").format(instance, method_name, bstack1l1llll1111_opy_, bstack1l1ll1llll1_opy_))
        if bstack1l1llll1111_opy_ == bstack1llll1lll11_opy_.bstack1lllll1l11l_opy_:
            if bstack1l1ll1llll1_opy_ == bstack1llll1ll111_opy_.POST and not bstack1lllll111l1_opy_.bstack1llll11llll_opy_ in instance.data:
                session_id = getattr(target, bstack1l1lll1_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠣᕘ"), None)
                if session_id:
                    instance.data[bstack1lllll111l1_opy_.bstack1llll11llll_opy_] = session_id
        elif (
            bstack1l1llll1111_opy_ == bstack1llll1lll11_opy_.bstack1llllllllll_opy_
            and bstack1lllll111l1_opy_.bstack1lllll11111_opy_(*args) == bstack1lllll111l1_opy_.bstack1llll1l11ll_opy_
        ):
            if bstack1l1ll1llll1_opy_ == bstack1llll1ll111_opy_.PRE:
                hub_url = bstack1lllll111l1_opy_.bstack111ll1ll1l_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lllll111l1_opy_.bstack1lll1ll1ll1_opy_: hub_url,
                            bstack1lllll111l1_opy_.bstack1lll11ll11l_opy_: bstack1lllll111l1_opy_.bstack1lll111l111_opy_(hub_url),
                            bstack1lllll111l1_opy_.bstack1llll1l1ll1_opy_: int(
                                os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠧᕙ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1lll11lll_opy_ = bstack1lllll111l1_opy_.bstack1l1lll1l1ll_opy_(*args)
                bstack11lllll111l_opy_ = bstack1l1lll11lll_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᕚ"), None) if bstack1l1lll11lll_opy_ else None
                if isinstance(bstack11lllll111l_opy_, dict):
                    instance.data[bstack1lllll111l1_opy_.bstack11llll1ll1l_opy_] = copy.deepcopy(bstack11lllll111l_opy_)
                    instance.data[bstack1lllll111l1_opy_.bstack1lll1ll1111_opy_] = bstack11lllll111l_opy_
            elif bstack1l1ll1llll1_opy_ == bstack1llll1ll111_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1l1lll1_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࠨᕛ"), dict()).get(bstack1l1lll1_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡋࡧࠦᕜ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lllll111l1_opy_.bstack1llll11llll_opy_: framework_session_id,
                                bstack1lllll111l1_opy_.bstack11llll1llll_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1llll1111_opy_ == bstack1llll1lll11_opy_.bstack1llllllllll_opy_
            and bstack1lllll111l1_opy_.bstack1lllll11111_opy_(*args) == bstack1lllll111l1_opy_.bstack11lllll1l1l_opy_
            and bstack1l1ll1llll1_opy_ == bstack1llll1ll111_opy_.POST
        ):
            instance.data[bstack1lllll111l1_opy_.bstack11lllll1111_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1lll11l11_opy_ in bstack1lllll111l1_opy_.bstack1l1111l11l1_opy_:
            bstack1l1ll1lll11_opy_ = None
            for callback in bstack1lllll111l1_opy_.bstack1l1111l11l1_opy_[bstack1l1lll11l11_opy_]:
                try:
                    bstack1l1lll111l1_opy_ = callback(self, target, exec, bstack1lllll1llll_opy_, result, *args, **kwargs)
                    if bstack1l1ll1lll11_opy_ == None:
                        bstack1l1ll1lll11_opy_ = bstack1l1lll111l1_opy_
                except Exception as e:
                    self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠡ࡫ࡱࡺࡴࡱࡩ࡯ࡩࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࠢᕝ") + str(e) + bstack1l1lll1_opy_ (u"ࠥࠦᕞ"))
                    traceback.print_exc()
            if bstack1l1llll1111_opy_ == bstack1llll1lll11_opy_.QUIT:
                if bstack1l1ll1llll1_opy_ == bstack1llll1ll111_opy_.POST:
                    bstack1ll1l11l111_opy_ = bstack1lll111ll11_opy_.get_state(instance, EVENTS.bstack11lll1l11l_opy_.value)
                    if bstack1ll1l11l111_opy_!=None:
                        bstack1llll1ll11l_opy_.end(EVENTS.bstack11lll1l11l_opy_.value, bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᕟ"), bstack1ll1l11l111_opy_+bstack1l1lll1_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᕠ"), True, None)
            if bstack1l1ll1llll1_opy_ == bstack1llll1ll111_opy_.PRE and callable(bstack1l1ll1lll11_opy_):
                return bstack1l1ll1lll11_opy_
            elif bstack1l1ll1llll1_opy_ == bstack1llll1ll111_opy_.POST and bstack1l1ll1lll11_opy_:
                return bstack1l1ll1lll11_opy_
    def bstack1l1lll1l1l1_opy_(
        self, method_name, previous_state: bstack1llll1lll11_opy_, *args, **kwargs
    ) -> bstack1llll1lll11_opy_:
        if method_name == bstack1l1lll1_opy_ (u"ࠨ࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠣᕡ") or method_name == bstack1l1lll1_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᕢ"):
            return bstack1llll1lll11_opy_.bstack1lllll1l11l_opy_
        if method_name == bstack1l1lll1_opy_ (u"ࠣࡳࡸ࡭ࡹࠨᕣ"):
            return bstack1llll1lll11_opy_.QUIT
        if method_name == bstack1l1lll1_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࠥᕤ"):
            if previous_state != bstack1llll1lll11_opy_.NONE:
                command_name = bstack1lllll111l1_opy_.bstack1lllll11111_opy_(*args)
                if command_name == bstack1lllll111l1_opy_.bstack1llll1l11ll_opy_:
                    return bstack1llll1lll11_opy_.bstack1lllll1l11l_opy_
            return bstack1llll1lll11_opy_.bstack1llllllllll_opy_
        return bstack1llll1lll11_opy_.NONE