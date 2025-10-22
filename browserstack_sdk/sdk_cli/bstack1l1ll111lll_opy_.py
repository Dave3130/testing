# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1l11_opy_,
    bstack1lllll111l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1lllll_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1lllll1111l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll11lll1_opy_(bstack1lllll1111l_opy_):
    bstack1l1ll11l1l1_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1llll1lllll_opy_.bstack1llll1l1l11_opy_((bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1llll1lll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1lll1l_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll1111111_opy_(hub_url):
            if not bstack1l1ll11lll1_opy_.bstack1l1ll11l1l1_opy_:
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠤ࡯ࡳࡨࡧ࡬ࠡࡵࡨࡰ࡫࠳ࡨࡦࡣ࡯ࠤ࡫ࡲ࡯ࡸࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡪࡰࡩࡶࡦࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡪࡸࡦࡤࡻࡲ࡭࠿ࠥዧ") + str(hub_url) + bstack1lllll1l_opy_ (u"ࠥࠦየ"))
                bstack1l1ll11lll1_opy_.bstack1l1ll11l1l1_opy_ = True
            return
        command_name = f.bstack1l1ll1ll1l1_opy_(*args)
        bstack1l1ll1l1ll1_opy_ = f.bstack1l1lll1111l_opy_(*args)
        if command_name and command_name.lower() == bstack1lllll1l_opy_ (u"ࠦ࡫࡯࡮ࡥࡧ࡯ࡩࡲ࡫࡮ࡵࠤዩ") and bstack1l1ll1l1ll1_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1ll1l1ll1_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡻࡳࡪࡰࡪࠦዪ"), None), bstack1l1ll1l1ll1_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧያ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠢࡼࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫ࡽ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡳࡷࠦࡡࡳࡩࡶ࠲ࡺࡹࡩ࡯ࡩࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡴࡸࠠࡢࡴࡪࡷ࠳ࡼࡡ࡭ࡷࡨࡁࠧዬ") + str(locator_value) + bstack1lllll1l_opy_ (u"ࠣࠤይ"))
                return
            def bstack1l1ll111l1l_opy_(driver, bstack1l1ll111ll1_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll111ll1_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll11l111_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1lllll1l_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࠧዮ") + str(locator_value) + bstack1lllll1l_opy_ (u"ࠥࠦዯ"))
                    else:
                        self.logger.warning(bstack1lllll1l_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷ࠲ࡴ࡯࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡃࠢደ") + str(response) + bstack1lllll1l_opy_ (u"ࠧࠨዱ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll11l1ll_opy_(
                        driver, bstack1l1ll111ll1_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll111l1l_opy_.__name__ = command_name
            return bstack1l1ll111l1l_opy_
    def __1l1ll11l1ll_opy_(
        self,
        driver,
        bstack1l1ll111ll1_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll11l111_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡶࡵ࡭࡬࡭ࡥࡳࡧࡧ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࠨዲ") + str(locator_value) + bstack1lllll1l_opy_ (u"ࠢࠣዳ"))
                bstack1l1ll11ll1l_opy_ = self.bstack1l1ll11llll_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1lllll1l_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡨࡦࡣ࡯࡭ࡳ࡭࡟ࡳࡧࡶࡹࡱࡺ࠽ࠣዴ") + str(bstack1l1ll11ll1l_opy_) + bstack1lllll1l_opy_ (u"ࠤࠥድ"))
                if bstack1l1ll11ll1l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1lllll1l_opy_ (u"ࠥࡹࡸ࡯࡮ࡨࠤዶ"): bstack1l1ll11ll1l_opy_.locator_type,
                            bstack1lllll1l_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥዷ"): bstack1l1ll11ll1l_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll111ll1_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡏ࡟ࡅࡇࡅ࡙ࡌࠨዸ"), False):
                    self.logger.info(bstack11ll1l1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠮࡯࡬ࡷࡸ࡯࡮ࡨ࠼ࠣࡷࡱ࡫ࡥࡱࠪ࠶࠴࠮ࠦ࡬ࡦࡶࡷ࡭ࡳ࡭ࠠࡺࡱࡸࠤ࡮ࡴࡳࡱࡧࡦࡸࠥࡺࡨࡦࠢࡥࡶࡴࡽࡳࡦࡴࠣࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠦ࡬ࡰࡩࡶࠦዹ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1lllll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡰࡲ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠿ࠥዺ") + str(response) + bstack1lllll1l_opy_ (u"ࠣࠤዻ"))
        except Exception as err:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠾ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨዼ") + str(err) + bstack1lllll1l_opy_ (u"ࠥࠦዽ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll11l11l_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1l1ll11l111_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1lllll1l_opy_ (u"ࠦ࠵ࠨዾ"),
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1lllll1l_opy_ (u"ࠧࠨዿ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1lllllll111_opy_.AISelfHealStep(req)
            self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣጀ") + str(r) + bstack1lllll1l_opy_ (u"ࠢࠣጁ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨጂ") + str(e) + bstack1lllll1l_opy_ (u"ࠤࠥጃ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll11ll11_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1l1ll11llll_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1lllll1l_opy_ (u"ࠥ࠴ࠧጄ")):
        self.bstack1llll1lll11_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1lllllll111_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1lllll1l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨጅ") + str(r) + bstack1lllll1l_opy_ (u"ࠧࠨጆ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦጇ") + str(e) + bstack1lllll1l_opy_ (u"ࠢࠣገ"))
            traceback.print_exc()
            raise e