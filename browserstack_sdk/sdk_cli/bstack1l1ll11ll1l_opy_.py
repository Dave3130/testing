# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1111111lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1llll1l11ll_opy_,
    bstack1llll1l1l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1l11_opy_ import bstack1llll1l11l1_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll1l1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll11llll_opy_(bstack1lllll1l1l1_opy_):
    bstack1l1ll1l1l11_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1llll1l11l1_opy_.bstack1lllll11111_opy_((bstack1llllll1111_opy_.bstack1llllll1lll_opy_, bstack1llll1l11ll_opy_.PRE), self.bstack1llll1ll11l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1ll11l_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllll1ll_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll11111l1_opy_(hub_url):
            if not bstack1l1ll11llll_opy_.bstack1l1ll1l1l11_opy_:
                self.logger.warning(bstack11111_opy_ (u"ࠤ࡯ࡳࡨࡧ࡬ࠡࡵࡨࡰ࡫࠳ࡨࡦࡣ࡯ࠤ࡫ࡲ࡯ࡸࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡪࡰࡩࡶࡦࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡪࡸࡦࡤࡻࡲ࡭࠿ࠥ኶") + str(hub_url) + bstack11111_opy_ (u"ࠥࠦ኷"))
                bstack1l1ll11llll_opy_.bstack1l1ll1l1l11_opy_ = True
            return
        command_name = f.bstack1l1lll11l11_opy_(*args)
        bstack1l1lll1111l_opy_ = f.bstack1l1llll11ll_opy_(*args)
        if command_name and command_name.lower() == bstack11111_opy_ (u"ࠦ࡫࡯࡮ࡥࡧ࡯ࡩࡲ࡫࡮ࡵࠤኸ") and bstack1l1lll1111l_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1lll1111l_opy_.get(bstack11111_opy_ (u"ࠧࡻࡳࡪࡰࡪࠦኹ"), None), bstack1l1lll1111l_opy_.get(bstack11111_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧኺ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11111_opy_ (u"ࠢࡼࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫ࡽ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡳࡷࠦࡡࡳࡩࡶ࠲ࡺࡹࡩ࡯ࡩࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡴࡸࠠࡢࡴࡪࡷ࠳ࡼࡡ࡭ࡷࡨࡁࠧኻ") + str(locator_value) + bstack11111_opy_ (u"ࠣࠤኼ"))
                return
            def bstack1l1ll1l1ll1_opy_(driver, bstack1l1ll1l11ll_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll1l11ll_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll11lll1_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack11111_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࠧኽ") + str(locator_value) + bstack11111_opy_ (u"ࠥࠦኾ"))
                    else:
                        self.logger.warning(bstack11111_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷ࠲ࡴ࡯࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡃࠢ኿") + str(response) + bstack11111_opy_ (u"ࠧࠨዀ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1l1lll_opy_(
                        driver, bstack1l1ll1l11ll_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll1l1ll1_opy_.__name__ = command_name
            return bstack1l1ll1l1ll1_opy_
    def __1l1ll1l1lll_opy_(
        self,
        driver,
        bstack1l1ll1l11ll_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll11lll1_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack11111_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡶࡵ࡭࡬࡭ࡥࡳࡧࡧ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࠨ዁") + str(locator_value) + bstack11111_opy_ (u"ࠢࠣዂ"))
                bstack1l1ll1l111l_opy_ = self.bstack1l1ll1l1l1l_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11111_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡨࡦࡣ࡯࡭ࡳ࡭࡟ࡳࡧࡶࡹࡱࡺ࠽ࠣዃ") + str(bstack1l1ll1l111l_opy_) + bstack11111_opy_ (u"ࠤࠥዄ"))
                if bstack1l1ll1l111l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11111_opy_ (u"ࠥࡹࡸ࡯࡮ࡨࠤዅ"): bstack1l1ll1l111l_opy_.locator_type,
                            bstack11111_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥ዆"): bstack1l1ll1l111l_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll1l11ll_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡏ࡟ࡅࡇࡅ࡙ࡌࠨ዇"), False):
                    self.logger.info(bstack1lll1ll11ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠮࡯࡬ࡷࡸ࡯࡮ࡨ࠼ࠣࡷࡱ࡫ࡥࡱࠪ࠶࠴࠮ࠦ࡬ࡦࡶࡷ࡭ࡳ࡭ࠠࡺࡱࡸࠤ࡮ࡴࡳࡱࡧࡦࡸࠥࡺࡨࡦࠢࡥࡶࡴࡽࡳࡦࡴࠣࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠦ࡬ࡰࡩࡶࠦወ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11111_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡰࡲ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠿ࠥዉ") + str(response) + bstack11111_opy_ (u"ࠣࠤዊ"))
        except Exception as err:
            self.logger.warning(bstack11111_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠾ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨዋ") + str(err) + bstack11111_opy_ (u"ࠥࠦዌ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll1l1111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l1ll11lll1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11111_opy_ (u"ࠦ࠵ࠨው"),
    ):
        self.bstack1lllll1lll1_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11111_opy_ (u"ࠧࠨዎ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll1lll11_opy_.AISelfHealStep(req)
            self.logger.info(bstack11111_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣዏ") + str(r) + bstack11111_opy_ (u"ࠢࠣዐ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨዑ") + str(e) + bstack11111_opy_ (u"ࠤࠥዒ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll1l11l1_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l1ll1l1l1l_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11111_opy_ (u"ࠥ࠴ࠧዓ")):
        self.bstack1lllll1lll1_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll1lll11_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11111_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨዔ") + str(r) + bstack11111_opy_ (u"ࠧࠨዕ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦዖ") + str(e) + bstack11111_opy_ (u"ࠢࠣ዗"))
            traceback.print_exc()
            raise e