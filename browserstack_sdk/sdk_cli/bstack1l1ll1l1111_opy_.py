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
from browserstack_sdk.sdk_cli.bstack1llllll1111_opy_ import bstack111111ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack111111111l_opy_,
    bstack111111lll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1lllll11ll1_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll1111_opy_ import bstack111111ll11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll1ll1l1_opy_(bstack111111ll11_opy_):
    bstack1l1ll1l11ll_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lllll11ll1_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_, bstack111111111l_opy_.PRE), self.bstack1llllll1lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llllll1lll_opy_(
        self,
        f: bstack1lllll11ll1_opy_,
        driver: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll1111l1l_opy_(hub_url):
            if not bstack1l1ll1ll1l1_opy_.bstack1l1ll1l11ll_opy_:
                self.logger.warning(bstack1ll11_opy_ (u"ࠦࡱࡵࡣࡢ࡮ࠣࡷࡪࡲࡦ࠮ࡪࡨࡥࡱࠦࡦ࡭ࡱࡺࠤࡩ࡯ࡳࡢࡤ࡯ࡩࡩࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢ࡬ࡲ࡫ࡸࡡࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧ዆") + str(hub_url) + bstack1ll11_opy_ (u"ࠧࠨ዇"))
                bstack1l1ll1ll1l1_opy_.bstack1l1ll1l11ll_opy_ = True
            return
        command_name = f.bstack1l1lll11ll1_opy_(*args)
        bstack1l1llll1111_opy_ = f.bstack1l1lll11111_opy_(*args)
        if command_name and command_name.lower() == bstack1ll11_opy_ (u"ࠨࡦࡪࡰࡧࡩࡱ࡫࡭ࡦࡰࡷࠦወ") and bstack1l1llll1111_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1llll1111_opy_.get(bstack1ll11_opy_ (u"ࠢࡶࡵ࡬ࡲ࡬ࠨዉ"), None), bstack1l1llll1111_opy_.get(bstack1ll11_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢዊ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1ll11_opy_ (u"ࠤࡾࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦࡿ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠥࡵࡲࠡࡣࡵ࡫ࡸ࠴ࡵࡴ࡫ࡱ࡫ࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡯ࡳࠢࡤࡶ࡬ࡹ࠮ࡷࡣ࡯ࡹࡪࡃࠢዋ") + str(locator_value) + bstack1ll11_opy_ (u"ࠥࠦዌ"))
                return
            def bstack1l1ll1l11l1_opy_(driver, bstack1l1ll1l1l11_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll1l1l11_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll1ll111_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1ll11_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࠢው") + str(locator_value) + bstack1ll11_opy_ (u"ࠧࠨዎ"))
                    else:
                        self.logger.warning(bstack1ll11_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹ࠭࡯ࡱ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠾ࠤዏ") + str(response) + bstack1ll11_opy_ (u"ࠢࠣዐ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1ll11l_opy_(
                        driver, bstack1l1ll1l1l11_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll1l11l1_opy_.__name__ = command_name
            return bstack1l1ll1l11l1_opy_
    def __1l1ll1ll11l_opy_(
        self,
        driver,
        bstack1l1ll1l1l11_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll1ll111_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1ll11_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡸࡷ࡯ࡧࡨࡧࡵࡩࡩࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࠣዑ") + str(locator_value) + bstack1ll11_opy_ (u"ࠤࠥዒ"))
                bstack1l1ll1l1l1l_opy_ = self.bstack1l1ll1l111l_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1ll11_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡪࡨࡥࡱ࡯࡮ࡨࡡࡵࡩࡸࡻ࡬ࡵ࠿ࠥዓ") + str(bstack1l1ll1l1l1l_opy_) + bstack1ll11_opy_ (u"ࠦࠧዔ"))
                if bstack1l1ll1l1l1l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1ll11_opy_ (u"ࠧࡻࡳࡪࡰࡪࠦዕ"): bstack1l1ll1l1l1l_opy_.locator_type,
                            bstack1ll11_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧዖ"): bstack1l1ll1l1l1l_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll1l1l11_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1ll11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡊࡡࡇࡉࡇ࡛ࡇࠣ዗"), False):
                    self.logger.info(bstack1lll1llllll_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠰ࡱ࡮ࡹࡳࡪࡰࡪ࠾ࠥࡹ࡬ࡦࡧࡳࠬ࠸࠶ࠩࠡ࡮ࡨࡸࡹ࡯࡮ࡨࠢࡼࡳࡺࠦࡩ࡯ࡵࡳࡩࡨࡺࠠࡵࡪࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࠡ࡮ࡲ࡫ࡸࠨዘ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1ll11_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰ࡲࡴ࠳ࡳࡤࡴ࡬ࡴࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥࡾࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࡁࠧዙ") + str(response) + bstack1ll11_opy_ (u"ࠥࠦዚ"))
        except Exception as err:
            self.logger.warning(bstack1ll11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡲࡦࡵࡸࡰࡹࡀࠠࡦࡴࡵࡳࡷࡀࠠࠣዛ") + str(err) + bstack1ll11_opy_ (u"ࠧࠨዜ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll1l1ll1_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1l1ll1ll111_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1ll11_opy_ (u"ࠨ࠰ࠣዝ"),
    ):
        self.bstack1111111l1l_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1ll11_opy_ (u"ࠢࠣዞ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llllll111l_opy_.AISelfHealStep(req)
            self.logger.info(bstack1ll11_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥዟ") + str(r) + bstack1ll11_opy_ (u"ࠤࠥዠ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣዡ") + str(e) + bstack1ll11_opy_ (u"ࠦࠧዢ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll1l1lll_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1l1ll1l111l_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1ll11_opy_ (u"ࠧ࠶ࠢዣ")):
        self.bstack1111111l1l_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llllll111l_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1ll11_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣዤ") + str(r) + bstack1ll11_opy_ (u"ࠢࠣዥ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨዦ") + str(e) + bstack1ll11_opy_ (u"ࠤࠥዧ"))
            traceback.print_exc()
            raise e