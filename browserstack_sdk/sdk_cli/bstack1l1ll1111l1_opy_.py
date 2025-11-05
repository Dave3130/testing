# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import (
    bstack1llll1l1ll1_opy_,
    bstack1llll11llll_opy_,
    bstack1llll111l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1ll111_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll111l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll111l1l_opy_(bstack1lllll111l1_opy_):
    bstack1l1ll111ll1_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1llll1ll111_opy_.bstack1lllll1l11l_opy_((bstack1llll1l1ll1_opy_.bstack1llll1lll11_opy_, bstack1llll11llll_opy_.PRE), self.bstack1lllll1ll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll1ll1l_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1ll1llll1ll_opy_(hub_url):
            if not bstack1l1ll111l1l_opy_.bstack1l1ll111ll1_opy_:
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠣ࡮ࡲࡧࡦࡲࠠࡴࡧ࡯ࡪ࠲࡮ࡥࡢ࡮ࠣࡪࡱࡵࡷࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡩ࡯ࡨࡵࡥࠥࡹࡥࡴࡵ࡬ࡳࡳࡹࠠࡩࡷࡥࡣࡺࡸ࡬࠾ࠤዻ") + str(hub_url) + bstack11ll1ll_opy_ (u"ࠤࠥዼ"))
                bstack1l1ll111l1l_opy_.bstack1l1ll111ll1_opy_ = True
            return
        command_name = f.bstack1l1ll1lll1l_opy_(*args)
        bstack1l1lll11l1l_opy_ = f.bstack1l1ll1l1ll1_opy_(*args)
        if command_name and command_name.lower() == bstack11ll1ll_opy_ (u"ࠥࡪ࡮ࡴࡤࡦ࡮ࡨࡱࡪࡴࡴࠣዽ") and bstack1l1lll11l1l_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1lll11l1l_opy_.get(bstack11ll1ll_opy_ (u"ࠦࡺࡹࡩ࡯ࡩࠥዾ"), None), bstack1l1lll11l1l_opy_.get(bstack11ll1ll_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦዿ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠨࡻࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࢃ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠢࡲࡶࠥࡧࡲࡨࡵ࠱ࡹࡸ࡯࡮ࡨ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡳࡷࠦࡡࡳࡩࡶ࠲ࡻࡧ࡬ࡶࡧࡀࠦጀ") + str(locator_value) + bstack11ll1ll_opy_ (u"ࠢࠣጁ"))
                return
            def bstack1l1ll1111ll_opy_(driver, bstack1l1ll11l11l_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll11l11l_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll111lll_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack11ll1ll_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴ࠯ࡶࡧࡷ࡯ࡰࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࠦጂ") + str(locator_value) + bstack11ll1ll_opy_ (u"ࠤࠥጃ"))
                    else:
                        self.logger.warning(bstack11ll1ll_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶ࠱ࡳࡵ࠭ࡴࡥࡵ࡭ࡵࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦࡿࠣࡶࡪࡹࡰࡰࡰࡶࡩࡂࠨጄ") + str(response) + bstack11ll1ll_opy_ (u"ࠦࠧጅ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll111111_opy_(
                        driver, bstack1l1ll11l11l_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll1111ll_opy_.__name__ = command_name
            return bstack1l1ll1111ll_opy_
    def __1l1ll111111_opy_(
        self,
        driver,
        bstack1l1ll11l11l_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll111lll_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack11ll1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡵࡴ࡬࡫࡬࡫ࡲࡦࡦ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࠧጆ") + str(locator_value) + bstack11ll1ll_opy_ (u"ࠨࠢጇ"))
                bstack1l1ll111l11_opy_ = self.bstack1l1ll11111l_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11ll1ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡵࡩࡸࡻ࡬ࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࢁࠥ࡮ࡥࡢ࡮࡬ࡲ࡬ࡥࡲࡦࡵࡸࡰࡹࡃࠢገ") + str(bstack1l1ll111l11_opy_) + bstack11ll1ll_opy_ (u"ࠣࠤጉ"))
                if bstack1l1ll111l11_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11ll1ll_opy_ (u"ࠤࡸࡷ࡮ࡴࡧࠣጊ"): bstack1l1ll111l11_opy_.locator_type,
                            bstack11ll1ll_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤጋ"): bstack1l1ll111l11_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll11l11l_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡎࡥࡄࡆࡄࡘࡋࠧጌ"), False):
                    self.logger.info(bstack1lll1ll1l11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡳࡧࡶࡹࡱࡺ࠭࡮࡫ࡶࡷ࡮ࡴࡧ࠻ࠢࡶࡰࡪ࡫ࡰࠩ࠵࠳࠭ࠥࡲࡥࡵࡶ࡬ࡲ࡬ࠦࡹࡰࡷࠣ࡭ࡳࡹࡰࡦࡥࡷࠤࡹ࡮ࡥࠡࡤࡵࡳࡼࡹࡥࡳࠢࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࠥࡲ࡯ࡨࡵࠥግ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11ll1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭࡯ࡱ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠾ࠤጎ") + str(response) + bstack11ll1ll_opy_ (u"ࠢࠣጏ"))
        except Exception as err:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠽ࠤࡪࡸࡲࡰࡴ࠽ࠤࠧጐ") + str(err) + bstack11ll1ll_opy_ (u"ࠤࠥ጑"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll11l1l1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1l1ll111lll_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11ll1ll_opy_ (u"ࠥ࠴ࠧጒ"),
    ):
        self.bstack1llllll1ll1_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11ll1ll_opy_ (u"ࠦࠧጓ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llllll1l1l_opy_.AISelfHealStep(req)
            self.logger.info(bstack11ll1ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢጔ") + str(r) + bstack11ll1ll_opy_ (u"ࠨࠢጕ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ጖") + str(e) + bstack11ll1ll_opy_ (u"ࠣࠤ጗"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll11l111_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1l1ll11111l_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11ll1ll_opy_ (u"ࠤ࠳ࠦጘ")):
        self.bstack1llllll1ll1_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llllll1l1l_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11ll1ll_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧጙ") + str(r) + bstack11ll1ll_opy_ (u"ࠦࠧጚ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥጛ") + str(e) + bstack11ll1ll_opy_ (u"ࠨࠢጜ"))
            traceback.print_exc()
            raise e