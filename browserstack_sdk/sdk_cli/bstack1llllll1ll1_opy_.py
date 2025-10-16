# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1lll11ll1l1_opy_,
    bstack1111111l11_opy_,
    bstack1llll1ll1ll_opy_,
    bstack1lllll1lll1_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
from bstack_utils.constants import EVENTS
class bstack1lllll1ll11_opy_(bstack1lll11ll1l1_opy_):
    bstack1l1lll11111_opy_ = bstack1lllll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᔱ")
    NAME = bstack1lllll1_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥᔲ")
    bstack1lll1l111l1_opy_ = bstack1lllll1_opy_ (u"ࠤ࡫ࡹࡧࡥࡵࡳ࡮ࠥᔳ")
    bstack1llll1l1l11_opy_ = bstack1lllll1_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᔴ")
    bstack11lllll111l_opy_ = bstack1lllll1_opy_ (u"ࠦ࡮ࡴࡰࡶࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᔵ")
    bstack1llll11l111_opy_ = bstack1lllll1_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᔶ")
    bstack1lll11ll1ll_opy_ = bstack1lllll1_opy_ (u"ࠨࡩࡴࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡪࡸࡦࠧᔷ")
    bstack11lllll1l1l_opy_ = bstack1lllll1_opy_ (u"ࠢࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠦᔸ")
    bstack11lllll11ll_opy_ = bstack1lllll1_opy_ (u"ࠣࡧࡱࡨࡪࡪ࡟ࡢࡶࠥᔹ")
    bstack1111111ll1_opy_ = bstack1lllll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࠥᔺ")
    bstack1lllll11l11_opy_ = bstack1lllll1_opy_ (u"ࠥࡲࡪࡽࡳࡦࡵࡶ࡭ࡴࡴࠢᔻ")
    bstack11llllll111_opy_ = bstack1lllll1_opy_ (u"ࠦ࡬࡫ࡴࠣᔼ")
    bstack1l11l1l1l11_opy_ = bstack1lllll1_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᔽ")
    bstack1l1llll1l1l_opy_ = bstack1lllll1_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࠤᔾ")
    bstack1l1lll11lll_opy_ = bstack1lllll1_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࡤࡷࡾࡴࡣࠣᔿ")
    bstack11lllll1lll_opy_ = bstack1lllll1_opy_ (u"ࠣࡳࡸ࡭ࡹࠨᕀ")
    bstack1l1111l11ll_opy_: Dict[str, List[Callable]] = dict()
    bstack1llll1llll1_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack111111111l_opy_: Any
    bstack1l1lll1ll11_opy_: Dict
    def __init__(
        self,
        bstack1llll1llll1_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack111111111l_opy_: Dict[str, Any],
        methods=[bstack1lllll1_opy_ (u"ࠤࡢࡣ࡮ࡴࡩࡵࡡࡢࠦᕁ"), bstack1lllll1_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࠥᕂ"), bstack1lllll1_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᕃ"), bstack1lllll1_opy_ (u"ࠧࡷࡵࡪࡶࠥᕄ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1llll1llll1_opy_ = bstack1llll1llll1_opy_
        self.platform_index = platform_index
        self.bstack1l1llll1ll1_opy_(methods)
        self.bstack111111111l_opy_ = bstack111111111l_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll11ll1l1_opy_.get_data(bstack1lllll1ll11_opy_.bstack1llll1l1l11_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll11ll1l1_opy_.get_data(bstack1lllll1ll11_opy_.bstack1lll1l111l1_opy_, target, strict)
    @staticmethod
    def bstack11lllll1ll1_opy_(target: object, strict=True):
        return bstack1lll11ll1l1_opy_.get_data(bstack1lllll1ll11_opy_.bstack11lllll111l_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll11ll1l1_opy_.get_data(bstack1lllll1ll11_opy_.bstack1llll11l111_opy_, target, strict)
    @staticmethod
    def bstack1lll11l1111_opy_(instance: bstack1111111l11_opy_) -> bool:
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1lllll1ll11_opy_.bstack1lll11ll1ll_opy_, False)
    @staticmethod
    def bstack1l1lll1llll_opy_(instance: bstack1111111l11_opy_, default_value=None):
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1lllll1ll11_opy_.bstack1lll1l111l1_opy_, default_value)
    @staticmethod
    def bstack1l1lll11l11_opy_(instance: bstack1111111l11_opy_, default_value=None):
        return bstack1lll11ll1l1_opy_.get_state(instance, bstack1lllll1ll11_opy_.bstack1llll11l111_opy_, default_value)
    @staticmethod
    def bstack1lll111l11l_opy_(hub_url: str, bstack11lllll1l11_opy_=bstack1lllll1_opy_ (u"ࠨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥᕅ")):
        try:
            bstack11lllll1111_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11lllll1111_opy_.endswith(bstack11lllll1l11_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1ll1lllll_opy_(method_name: str):
        return method_name == bstack1lllll1_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᕆ")
    @staticmethod
    def bstack1llllll111l_opy_(method_name: str, *args):
        return (
            bstack1lllll1ll11_opy_.bstack1l1ll1lllll_opy_(method_name)
            and bstack1lllll1ll11_opy_.bstack1llllllllll_opy_(*args) == bstack1lllll1ll11_opy_.bstack1lllll11l11_opy_
        )
    @staticmethod
    def bstack1l1lll111ll_opy_(method_name: str, *args):
        if not bstack1lllll1ll11_opy_.bstack1l1ll1lllll_opy_(method_name):
            return False
        if not bstack1lllll1ll11_opy_.bstack1l1llll1l1l_opy_ in bstack1lllll1ll11_opy_.bstack1llllllllll_opy_(*args):
            return False
        bstack1l1llll1l11_opy_ = bstack1lllll1ll11_opy_.bstack1l1lll1l111_opy_(*args)
        return bstack1l1llll1l11_opy_ and bstack1lllll1_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣᕇ") in bstack1l1llll1l11_opy_ and bstack1lllll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᕈ") in bstack1l1llll1l11_opy_[bstack1lllll1_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᕉ")]
    @staticmethod
    def bstack1l1lll1l1ll_opy_(method_name: str, *args):
        if not bstack1lllll1ll11_opy_.bstack1l1ll1lllll_opy_(method_name):
            return False
        if not bstack1lllll1ll11_opy_.bstack1l1llll1l1l_opy_ in bstack1lllll1ll11_opy_.bstack1llllllllll_opy_(*args):
            return False
        bstack1l1llll1l11_opy_ = bstack1lllll1ll11_opy_.bstack1l1lll1l111_opy_(*args)
        return (
            bstack1l1llll1l11_opy_
            and bstack1lllll1_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᕊ") in bstack1l1llll1l11_opy_
            and bstack1lllll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡦࡶ࡮ࡶࡴࠣᕋ") in bstack1l1llll1l11_opy_[bstack1lllll1_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨᕌ")]
        )
    @staticmethod
    def bstack1llllllllll_opy_(*args):
        return str(bstack1lllll1ll11_opy_.bstack1l1lll111l1_opy_(*args)).lower()
    @staticmethod
    def bstack1l1lll111l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll1l111_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack1lll1ll111_opy_(driver):
        command_executor = getattr(driver, bstack1lllll1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᕍ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1lllll1_opy_ (u"ࠣࡡࡸࡶࡱࠨᕎ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1lllll1_opy_ (u"ࠤࡢࡧࡱ࡯ࡥ࡯ࡶࡢࡧࡴࡴࡦࡪࡩࠥᕏ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1lllll1_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡢࡷࡪࡸࡶࡦࡴࡢࡥࡩࡪࡲࠣᕐ"), None)
        return hub_url
    def bstack111111ll1l_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1lllll1_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᕑ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1lllll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᕒ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1lllll1_opy_ (u"ࠨ࡟ࡶࡴ࡯ࠦᕓ")):
                setattr(command_executor, bstack1lllll1_opy_ (u"ࠢࡠࡷࡵࡰࠧᕔ"), hub_url)
                result = True
        if result:
            self.bstack1llll1llll1_opy_ = hub_url
            bstack1lllll1ll11_opy_.bstack1lllll1l11l_opy_(instance, bstack1lllll1ll11_opy_.bstack1lll1l111l1_opy_, hub_url)
            bstack1lllll1ll11_opy_.bstack1lllll1l11l_opy_(
                instance, bstack1lllll1ll11_opy_.bstack1lll11ll1ll_opy_, bstack1lllll1ll11_opy_.bstack1lll111l11l_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1lll1lll1_opy_(bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_]):
        return bstack1lllll1_opy_ (u"ࠣ࠼ࠥᕕ").join((bstack1llll1ll1ll_opy_(bstack1lllll111ll_opy_[0]).name, bstack1lllll1lll1_opy_(bstack1lllll111ll_opy_[1]).name))
    @staticmethod
    def bstack11111111ll_opy_(bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_], callback: Callable):
        bstack1l1llll1111_opy_ = bstack1lllll1ll11_opy_.bstack1l1lll1lll1_opy_(bstack1lllll111ll_opy_)
        if not bstack1l1llll1111_opy_ in bstack1lllll1ll11_opy_.bstack1l1111l11ll_opy_:
            bstack1lllll1ll11_opy_.bstack1l1111l11ll_opy_[bstack1l1llll1111_opy_] = []
        bstack1lllll1ll11_opy_.bstack1l1111l11ll_opy_[bstack1l1llll1111_opy_].append(callback)
    def bstack1l1llll11ll_opy_(self, instance: bstack1111111l11_opy_, method_name: str, bstack1l1lll1l11l_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1lllll1_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᕖ")):
            return
        cmd = args[0] if method_name == bstack1lllll1_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦᕗ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11lllll11l1_opy_ = bstack1lllll1_opy_ (u"ࠦ࠿ࠨᕘ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠿ࠨᕙ") + bstack11lllll11l1_opy_, bstack1l1lll1l11l_opy_)
    def bstack1l1lll11l1l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll1ll1l_opy_, bstack1l1llll111l_opy_ = bstack1lllll111ll_opy_
        bstack1l1llll1111_opy_ = bstack1lllll1ll11_opy_.bstack1l1lll1lll1_opy_(bstack1lllll111ll_opy_)
        self.logger.debug(bstack1lllll1_opy_ (u"ࠨ࡯࡯ࡡ࡫ࡳࡴࡱ࠺ࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᕚ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠢࠣᕛ"))
        if bstack1l1lll1ll1l_opy_ == bstack1llll1ll1ll_opy_.QUIT:
            if bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.PRE:
                bstack1ll1l1l1111_opy_ = bstack1lllllllll1_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack1111llllll_opy_.value)
                bstack1lll11ll1l1_opy_.bstack1lllll1l11l_opy_(instance, EVENTS.bstack1111llllll_opy_.value, bstack1ll1l1l1111_opy_)
                self.logger.debug(bstack1lllll1_opy_ (u"ࠣ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠥ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠧᕜ").format(instance, method_name, bstack1l1lll1ll1l_opy_, bstack1l1llll111l_opy_))
        if bstack1l1lll1ll1l_opy_ == bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_:
            if bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.POST and not bstack1lllll1ll11_opy_.bstack1llll1l1l11_opy_ in instance.data:
                session_id = getattr(target, bstack1lllll1_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨᕝ"), None)
                if session_id:
                    instance.data[bstack1lllll1ll11_opy_.bstack1llll1l1l11_opy_] = session_id
        elif (
            bstack1l1lll1ll1l_opy_ == bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_
            and bstack1lllll1ll11_opy_.bstack1llllllllll_opy_(*args) == bstack1lllll1ll11_opy_.bstack1lllll11l11_opy_
        ):
            if bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.PRE:
                hub_url = bstack1lllll1ll11_opy_.bstack1lll1ll111_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lllll1ll11_opy_.bstack1lll1l111l1_opy_: hub_url,
                            bstack1lllll1ll11_opy_.bstack1lll11ll1ll_opy_: bstack1lllll1ll11_opy_.bstack1lll111l11l_opy_(hub_url),
                            bstack1lllll1ll11_opy_.bstack1111111ll1_opy_: int(
                                os.environ.get(bstack1lllll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥᕞ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1llll1l11_opy_ = bstack1lllll1ll11_opy_.bstack1l1lll1l111_opy_(*args)
                bstack11lllll1ll1_opy_ = bstack1l1llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᕟ"), None) if bstack1l1llll1l11_opy_ else None
                if isinstance(bstack11lllll1ll1_opy_, dict):
                    instance.data[bstack1lllll1ll11_opy_.bstack11lllll111l_opy_] = copy.deepcopy(bstack11lllll1ll1_opy_)
                    instance.data[bstack1lllll1ll11_opy_.bstack1llll11l111_opy_] = bstack11lllll1ll1_opy_
            elif bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1lllll1_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦᕠ"), dict()).get(bstack1lllll1_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࡉࡥࠤᕡ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lllll1ll11_opy_.bstack1llll1l1l11_opy_: framework_session_id,
                                bstack1lllll1ll11_opy_.bstack11lllll1l1l_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1lll1ll1l_opy_ == bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_
            and bstack1lllll1ll11_opy_.bstack1llllllllll_opy_(*args) == bstack1lllll1ll11_opy_.bstack11lllll1lll_opy_
            and bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.POST
        ):
            instance.data[bstack1lllll1ll11_opy_.bstack11lllll11ll_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1llll1111_opy_ in bstack1lllll1ll11_opy_.bstack1l1111l11ll_opy_:
            bstack1l1lll1111l_opy_ = None
            for callback in bstack1lllll1ll11_opy_.bstack1l1111l11ll_opy_[bstack1l1llll1111_opy_]:
                try:
                    bstack1l1lll11ll1_opy_ = callback(self, target, exec, bstack1lllll111ll_opy_, result, *args, **kwargs)
                    if bstack1l1lll1111l_opy_ == None:
                        bstack1l1lll1111l_opy_ = bstack1l1lll11ll1_opy_
                except Exception as e:
                    self.logger.error(bstack1lllll1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࠧᕢ") + str(e) + bstack1lllll1_opy_ (u"ࠣࠤᕣ"))
                    traceback.print_exc()
            if bstack1l1lll1ll1l_opy_ == bstack1llll1ll1ll_opy_.QUIT:
                if bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.POST:
                    bstack1ll1l1l1111_opy_ = bstack1lll11ll1l1_opy_.get_state(instance, EVENTS.bstack1111llllll_opy_.value)
                    if bstack1ll1l1l1111_opy_!=None:
                        bstack1lllllllll1_opy_.end(EVENTS.bstack1111llllll_opy_.value, bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᕤ"), bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᕥ"), True, None)
            if bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.PRE and callable(bstack1l1lll1111l_opy_):
                return bstack1l1lll1111l_opy_
            elif bstack1l1llll111l_opy_ == bstack1lllll1lll1_opy_.POST and bstack1l1lll1111l_opy_:
                return bstack1l1lll1111l_opy_
    def bstack1l1llll11l1_opy_(
        self, method_name, previous_state: bstack1llll1ll1ll_opy_, *args, **kwargs
    ) -> bstack1llll1ll1ll_opy_:
        if method_name == bstack1lllll1_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨᕦ") or method_name == bstack1lllll1_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᕧ"):
            return bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_
        if method_name == bstack1lllll1_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᕨ"):
            return bstack1llll1ll1ll_opy_.QUIT
        if method_name == bstack1lllll1_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᕩ"):
            if previous_state != bstack1llll1ll1ll_opy_.NONE:
                command_name = bstack1lllll1ll11_opy_.bstack1llllllllll_opy_(*args)
                if command_name == bstack1lllll1ll11_opy_.bstack1lllll11l11_opy_:
                    return bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_
            return bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_
        return bstack1llll1ll1ll_opy_.NONE